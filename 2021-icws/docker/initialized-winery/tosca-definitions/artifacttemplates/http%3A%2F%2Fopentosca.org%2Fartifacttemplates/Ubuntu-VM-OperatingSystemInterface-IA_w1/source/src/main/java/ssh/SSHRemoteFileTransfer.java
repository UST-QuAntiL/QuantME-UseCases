package ssh;

import java.io.File;
import java.io.InputStream;

import org.vngx.jsch.ChannelSftp;
import org.vngx.jsch.ChannelType;
import org.vngx.jsch.Session;

public class SSHRemoteFileTransfer {

	private final Session session;
	private final ChannelSftp sftp;

	public SSHRemoteFileTransfer(Session session) {
		this.session = session;
		try {
			this.sftp = (ChannelSftp) this.session.openChannel(ChannelType.SFTP.toString());
			this.sftp.connect();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}

	public void close() {
		this.sftp.disconnect();
		this.session.disconnect();
	}
	
	public boolean isConnected() {
		return !this.session.isConnected() || !this.sftp.isConnected();
	}

	public void putFile(String sourceFilename, String destFilename) {
		if (isConnected()) {
			throw new RuntimeException("Not connected to host " + this.session.getHost());
		}
		if (!(new File(sourceFilename).exists())) {
			throw new RuntimeException("File " + sourceFilename + " does not exist.");
		}

		System.out.println("### transferSingelFile from " + sourceFilename + " to " + destFilename + " on " + this.session.getHost());

		try {
			this.sftp.put(sourceFilename, destFilename);
			
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}
	
	public void putFile(InputStream inputStream, String destFilename) {
		if (isConnected()) {
			throw new RuntimeException("Not connected to host " + this.session.getHost());
		}

		System.out.println("### Putting file to " + destFilename + " on " + this.session.getHost());

		try {
			this.sftp.put(inputStream, destFilename);
			
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}
	
	public void getFile(String sourceFilename, File destFile) {
		if (isConnected()) {
			throw new RuntimeException("Not connected to host " + this.session.getHost());
		}

		System.out.println("### retrieveSingelFile from " + this.session.getHost() + sourceFilename + " to " + destFile.getAbsolutePath() + ".");

		try {
			this.sftp.get(sourceFilename, destFile.getAbsolutePath());
			
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}
}
