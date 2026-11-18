class Task implements Runnable{
    public void run(){
        System.out.println("thread is running  " + Thread.currentThread().getName());
    }

}


public class inthrd  {
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(new Task() , "worker -1");
        t.start();
        Thread t2 = new Thread(() -> System.out.println("my thread ") );
        t2.start();
        t.join();
        System.out.println("mian done");
        
        
    }
    
}
