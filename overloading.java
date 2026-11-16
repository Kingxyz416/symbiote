class calc{
    int add(int a , int b){
        return a + b ;
    }
    int add(int a , int b , int c ){
        return a + b + c;
    }
    String add(String a ,  String b){
        return a + b ;
    }
}
class sci extends calc{
    @Override int add(int a , int b){
        return a + 1;
    }
}
public class overloading{
    public static void main (String[] args){
        calc c = new calc();
        System.out.println(c.add(2,5));
        System.out.println(c.add(2,5,3));
        System.out.println(c.add("ja","va"));
        sci s = new sci();
        System.out.println(s.add(2,6));
    }
}