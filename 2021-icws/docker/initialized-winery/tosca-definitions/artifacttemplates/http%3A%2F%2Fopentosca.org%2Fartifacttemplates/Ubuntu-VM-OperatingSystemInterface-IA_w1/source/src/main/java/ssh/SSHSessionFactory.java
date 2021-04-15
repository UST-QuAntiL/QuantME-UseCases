package ssh;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import org.vngx.jsch.JSch;
import org.vngx.jsch.Session;
import org.vngx.jsch.UserInfo;
import org.vngx.jsch.config.SessionConfig;
import org.vngx.jsch.exception.JSchException;
import org.vngx.jsch.userauth.IdentityManager;
import org.vngx.jsch.userauth.UserAuth;
import org.vngx.jsch.util.HostKey;
import org.vngx.jsch.util.KeyType;

public class SSHSessionFactory {
	
	/**
	 * Secure session creation which retries once, because in some cases the creation of the session does not work.
	 * @param host
	 * @param sshUser
	 * @param sshKey
	 * @return
	 */
	public static Session createSSHSession(String host, String sshUser, String sshKey) {
		// Create Session, retry once
		try {
			return SSHSessionFactory.createSSHSessionSingle(host, sshUser, sshKey);
		} catch(Exception e) {
			System.err.println("Failed to create SSH Session at first attempt (" + e + ") trying one more time.");
			return SSHSessionFactory.createSSHSessionSingle(host, sshUser, sshKey);
		}
	}
	
	private static Session createSSHSessionSingle(String host, String sshUser, String sshKey) {
		try {
			JSch jsch = JSch.getInstance();
			
			// Add to Host Key Repository & Identity Manager
			// ...by putting it into a temp file
			File keyFile = File.createTempFile("ssh", ".key");
			// Delete temp file when program exits.
			keyFile.deleteOnExit();
			
			// Write to temp file
			BufferedWriter out = new BufferedWriter(new FileWriter(keyFile));
			out.write(sshKey);
			out.close();
			
			IdentityManager.getManager().removeAllIdentities();
			IdentityManager.getManager().addIdentity(keyFile.getAbsolutePath());
			HostKey hostkey = new HostKey(host, KeyType.SSH_RSA, sshKey.getBytes());
			UserInfo ui = new UserInfo() {
				
				// Control flow should never be in on of these methods!!!
				
				@Override
				public void showMessage(String message) {
					throw new RuntimeException("UserInfo.showMessage: " + message + "\n"); 
				}
				
				@Override
				public boolean promptYesNo(String message) {
					throw new RuntimeException("UserInfo.promptYesNo: " + message + "\n");
				}
				
				@Override
				public boolean promptPassword(String message) {
					throw new RuntimeException("UserInfo.promptPassword: " + message + "\n");
				}
				
				@Override
				public boolean promptPassphrase(String message) {
					throw new RuntimeException("UserInfo.promptPassphrase: " + message + "\n");
				}
				
				@Override
				public String getPassword() {
					throw new RuntimeException("UserInfo.getPassword\n");
				}
				
				@Override
				public String getPassphrase() {
					throw new RuntimeException("UserInfo.getPassphrase\n");
				}
			};
			jsch.getHostKeyRepository().add(hostkey, ui);
			
			// Create Session
			Session session = jsch.createSession(sshUser, host, 22);
			session.setUserInfo(ui);
			session.getConfig().setProperty(SessionConfig.STRICT_HOST_KEY_CHECKING, "no");
			session.getConfig().setProperty(SessionConfig.PREFFERED_AUTHS, UserAuth.PUBLICKEY);
			
			// Let's go
			session.connect();
			
			return session;
			
		} catch (JSchException e) {
			throw new RuntimeException(e);
			
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}
