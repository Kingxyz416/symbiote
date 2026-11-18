class mythread extends Thread{
    @Override public void run(){
        for(int i=1 ; i < 5 ;i++){
            System.out.println("hiiiii");
        }
    }
}
class mythread1 extends Thread{
   @Override public void run(){
         for(int i=1 ; i < 5 ;i++){
            System.out.println("hello");
        
    }
}
}



public class thrd {
    public static void main(String[] args) {
        mythread t1 = new mythread();
        mythread1 t2 = new mythread1();
        t1.start();
        try{
            t1.join();
        }
        catch(InterruptedException e){
            System.out.println(e.getMessage());
        }
        t2.start();
    }
    
}
