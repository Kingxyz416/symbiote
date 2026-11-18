

class bank{
    double balance;
    long accno;
    public bank(double balance , long accno){
        this.balance = balance;
        this.accno = accno;

    }
    public void  view(){
        System.out.println(balance);
        if(balance<=100){
            System.out.println("add money to avoid the minimum balance fee");
        }
    }
    public void sc(double amount){
        try{
            if (amount < 0) {
                throw new IllegalArgumentException("Withdrawal amount cannot be negative");
            }
            if (amount > balance) {
                throw new ArithmeticException("Insufficient balance");
            }
            balance -= amount;
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }
        finally{
            view();
        }

    }
}
class bankexecp{
    public static void main(String[] args) {
        bank b = new bank(100,1145);
        b.sc(150);


    }
} 