import random

class ATM:

    user = "vimalgrace"
    passw = "Demo@123"
    balance = 1000
    
    def check_username_and_password(self):
        self.username = input("Enter username : ")
        self.password = input("Enter password : ")

        if self.username == self.user and self.password == self.passw:
            print("Login successfull")
            return True
        else:
            print("Incorrect login and password")
            return False
    
    def show_balance(self):
        if(self.generate_otp() == self.otp_check):
            print(f"Available balance : {self.balance}")
        else:
            print("Invalid OTP.")


    def withdraw_money(self):
        if(self.generate_otp() == self.otp_check):
            self.amount = int(input("Enter the amount to withdraw : "))

            if self.amount > 0:
                if self.amount <= self.balance:
                    self.balance = self.balance - self.amount
                    print(f"Rs.{self.amount} debited successfully.")
                else:
                    print("Low Balance")
            else:
                print("Invalid Amount")
        else:
            print("Invalid OTP.")

    
    def deposit_money(self):
        if(self.generate_otp() == self.otp_check):
            self.deposit_amount = int(input("Enter the amount to deposit : "))

            if self.deposit_amount > 0:
                self.balance = self.balance + self.deposit_amount
                print(f"Rs.{self.deposit_amount} credited successfully")
            else:
                print("Invalid amount")
        else:
            print("Invalid OTP.")

    def generate_otp(self):
        li = []
        for i in range(6):
            li.append(str(random.randint(0,9)))
        otp = "".join(li)
        print(f"Your one time password is : {otp}")

        self.otp_check = input("Enter the otp : ")
        return otp
        
            

    def start(self):

        if(self.check_username_and_password()):
            while True:
                print("-"*50)
                print(f"1.Show balance\n2.Withdraw Money\n3.Deposit Money\n4.Exit")
                print("-"*50)
                n = int(input("Enter the option : "))
                
                if(n == 1):
                    self.show_balance()
                elif(n == 2):
                    self.withdraw_money()
                elif(n == 3):
                    self.deposit_money()
                elif(n == 4):
                    print("Thank you. Come Again.")
                    break
                

machine = ATM()
machine.start()  
# machine.generate_otp() 
     
        











