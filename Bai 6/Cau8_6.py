print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
class Bank:
    Account_type = "Savings"
    
    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = "SBI ATM Machine"

    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        print("-------------------------------")
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 123:
            print(f"Account Holder: {self.name}")
            print(f"Account Number: {self.Account_Number}")
            self.Account()
        else:
            self.Error()

    def Error(self):
        print("Pin Incorrect. Please try again")
    
    def Account(self):
        print("Your Card Number is: XXXX XXXX XXXX 1237")
        print("Would you like to deposit/Withdraw/Check Balance?")
        print("""
        1) Balance
        2) Withdraw
        3) Deposit
        4) Quit
        """)
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Invalid input!")
            return
        
        if option == 1:
            self.Balance()
        elif option == 2:
            self.Withdraw()
        elif option == 3:
            self.Deposit()
        elif option == 4:
            print("Thank you! Visit again.")
        else:
            print("Invalid choice!")

    def Balance(self):
        print(f"Balance: {self.balance} VND")
        self.Account()

    def Withdraw(self):
        w = int(input("Please Enter Desired amount: "))
        if w > self.balance:
            print("Your transaction is cancelled due to")
            print("Amount is not sufficient in your account")
        else:
            self.balance -= w
            print(f"{w} VND Transaction is successful!")
            print(f"Your Balance: {self.balance} VND")
        self.Account()

    def Deposit(self):
        d = int(input("Please Enter Desired amount: "))
        self.balance += d
        print(f"{d} VND Transaction is successful!")
        print(f"Your Balance: {self.balance} VND")
        self.Account()


# Chạy chương trình
print("=== SBI ATM MACHINE ===")
t1 = Bank("Mahesh", 1453210145, 5000)
print(t1)
