package ssh;

import java.io.IOException;
import java.io.InputStream;
import java.io.StringWriter;

import org.apache.commons.io.IOUtils;
import org.vngx.jsch.ChannelExec;
import org.vngx.jsch.ChannelType;
import org.vngx.jsch.Session;
import org.vngx.jsch.exception.JSchException;

public class SSHRemoteCommandExec {
	
	private final Session session;
	private boolean connected = false;
	
	public SSHRemoteCommandExec(Session session) {
		this.session = session;
		this.connected = this.session.isConnected();
	}
	
	public void close() {
		this.session.disconnect();
		this.connected = false;
	}
	
	public String execute(String command) throws JSchException, IOException {
		if (!this.connected) {
			throw new RuntimeException("Not connected to host " + this.session.getHost());
		}
		System.out.println("### Executing: " + command + " on " + this.session.getHost());
		
		ChannelExec c = (ChannelExec) this.session.openChannel(ChannelType.EXEC.toString());
		c.setPty(true);
		c.setCommand(command + "\n");
		
		InputStream is = c.getInputStream();
		
		// Connect and read results
		// See: http://stackoverflow.com/questions/309424/read-convert-an-inputstream-to-a-string
		c.connect();
		StringWriter writer = new StringWriter();
		IOUtils.copy(is, writer, "utf8");
		c.disconnect();
		
		System.out.println("Done.");
		return writer.toString().replaceAll("[\\x00-\\x09\\x11\\x12\\x14-\\x1F\\x7F]", "");
	}
}
