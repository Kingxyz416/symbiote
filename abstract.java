abstract class animal{
    abstract void sound();
}
class dog extends animal{
    void sound(){
        System.out.println("woof");
    }
}
class cat extends animal{
    void sound(){
        System.out.println("meow");
    }
}
class AnimalDemo {
    public static void main(String[] args) {
        animal a = new dog();
        animal b = new cat();
        a.sound();
        b.sound();
        
    }
}