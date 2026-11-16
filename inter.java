interface caar{
    void drive();
}
interface plane{
    void fly();
}
class flyingcar implements caar , plane {
    @Override 
    public void drive(){
        System.out.println("could also drive");
    }
    public void fly(){
        System.out.println("can aslo fly");
    }
}
class inter{
    public static void main(String[] args){
        flyingcar a = new flyingcar();
        a.drive();
        a.fly();
    }
}