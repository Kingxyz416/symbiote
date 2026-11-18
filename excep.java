public class excep{
    public static void main(String[] args){
        int a[] = {10,20};
        try{
            int x = 10/0;
            System.out.println(x);
            
        }
        catch(ArithmeticException e){
            System.out.println("arithmetic exception  " + e.getMessage());
        }
        try{
            System.out.println(a[5]);
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("array index out of bound  " + e.getMessage());
        }
        finally{
            System.out.println("runs ");
        }

        
    }
}