class student{
    private String name;
    private long rollno;
    public void setdetails(String n, long v){
        name = n;
        rollno = v;
    }
    public String getname(){
        return name;
    }
    public long getrollno(){
        return rollno;
    }
    public static void main(String []args){
        student s = new student();
        s.setdetails("huzaifa", 2025310040L);
        System.out.println("Name: " + s.getname());
        System.out.println("Roll No: " + s.getrollno());
    }

}
