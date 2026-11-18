import java.io.IOException;

public class thr {
    static void agecheck(int age){
        if(age < 18){
            throw new ArithmeticException("not eligible to vote");
        }
        else{
            System.out.println("eligible");
        }
    }
    static void readfile() throws IOException {
        
        System.out.println(" file opend");
    }
    public static void main(String[] args) {
        try{
            agecheck(19);
            agecheck(10);

        }
        catch(ArithmeticException e){
            System.out.println(e.getMessage());
        }
        try{readfile();}
        catch(IOException e){
            System.out.println(e.getMessage());
        }

    }
}
