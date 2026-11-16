class vehical{
    int speed = 100;
    void start(){
        
        System.out.println("vehical starts ");
    }
}
class car extends vehical{
    ;
    void horn(){
        System.out.println("beep beep");
        
    }
    void fast(){
        System.out.println(super.speed);
    }
}
public class inheritance{
    public static void main  (String[] args){
        car c = new car();
        c.start();
        c.horn();
        c.fast();

    }
}