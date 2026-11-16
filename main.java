class bank{

    private double bankbalance;
    private String name;
    private long  accno;

    public bank(double bankbalance , String name , long accno ){
        this.bankbalance=bankbalance;
        this.name=name;
        this.accno=accno;
    }
    public void  viewdetail(){
        System.out.println(bankbalance);
        System.out.println(name);
        System.out.println(accno);

    }
    public void deposit(double amount){
        if (amount>0){
            bankbalance+=amount;
            System.out.println("sucsefully deposited ="+ amount);
        }
        else{
            System.out.println("enter valid amount ");
        }
    }
    
    public void withdraw(double amaount ){
        if(amaount<=0){
            System.out.println("enter valid amount ");
        }
        else if (amaount>bankbalance){
            System.out.println("insufficientfund");
        }
        else {
            bankbalance-= amaount;
            System.out.println("susccsefully withdrawn ="+ amaount);
        }

    }
}
class Main{
    public static void main (String[] Args){
        bank b1 = new bank(5000,"king",11004);
        b1.viewdetail();
        b1.deposit(100);
        b1.withdraw(300);
        b1.viewdetail();

        
    }
}
