import java.io.FileReader;
import java.io.IOException;

public class thrw {
    static void readfile() throws IOException{
        try (FileReader file = new FileReader("data.txt")) {
            while (file.read() != -1) {
                
            }
            System.out.println("file opened");
        }
    }
    public static void main(String[] args) {
        try{
            readfile();
        }
        catch(IOException e){
            System.out.println("not succesfull" + e.getMessage());

        }
        finally{
            System.out.println("continue ");
        }

    }
    
}
