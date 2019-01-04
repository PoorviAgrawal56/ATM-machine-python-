import time

def login(j,k):
    print("Starting login procedure")
    time.sleep(1)
    t=input("Enter your account number: ")
    y=input("Enter your PIN: ")
    f=open("D:\log.txt","a")
    f.write("customer login info:")
    f.write("\nAcc number:"+t)
    f.write("\nPIN:"+y)
    f.close()
    if(y==k and j==t):
        b=input('''What action do you want to perform
        1.balance enquiry
        2.cash withdrawl
        3.Fund transfer
        :''')
        if(b=='1'):
            f=open("D:\dem.txt","w")
            f.write("Balance=20000")
            f.close()
            print("Your available balance is INR 20000")
        elif(b=='2'):
            s=int(input("Enter the amount you want to withdraw: "))
            if(s<=20000):
                print("Please collect the cash ")
                f=open("D:\wthdrw.txt","a")
                f.write("Withdrawn Amount:")
                f.write(str(int(s)))
                f.close()
                time.sleep(2)
                print("Thank you for using the ATM")
            else:
                print("Insufficient Balance")
        elif(b=='3'):
            input("Enter the Bank name you want to transfer: ")
            input("Enter the account number associated: ")
            x=int(input("Enter the amount you want to transfer:"))
            if(x<=20000):
                print("Please wait while we transfer to the account")
                n=open("transfer.txt","w")
                n.write("Transfered Amount:")
                n.write(str(int(x)))
                n.close()
                time.sleep(2)
                print("Amount has been sucssfully transfered")
            else:
                print("Transfer amount is greater than Transfer Limit")
        else:
            print("You have selected wrong operation")
    else:
        print("Wrong PIN! Pls Register and come")
        l=input("Do you want to perform registration now? Y/N ")
        if(l=='Y'):
            print("Starting registration process please wait!")
            time.sleep(1)
            registr()
        else:
            print("Thank you for using our service")
        
def registr():
    f=open("D:/reg.txt","a")
    g=input("Enter your name:")
    h=input("Enter your age:")
    i=input("Enter your present address:")
    j=input("Enter your account number:")
    k=input("Enter your desired PIN:")
    f.write('Name:'+g)
    f.write('\nAge:'+h)
    f.write('\nAddress:'+i)
    f.write('\nAccount number:'+j)
    f.write('\nYour PIN is:'+k)
    f.write("\n")
    f.close()
    print("Your account has been created")
    login(j,k)

print("***Welcome To ATM***")
a=int(input('''What action do you wish to perform?
      Press 1 for login
      Press 2 for registration
      '''))
if(a==1):
    login(7,8)
elif(a==2):    
    registr()
else:
    print("Invalid operation")
