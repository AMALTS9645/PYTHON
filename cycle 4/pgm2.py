class Account:
    def __init__(self):
        self.balance=0
    def create(self):
        self.acno=int(input("Enter your Account no:"))
        self.name=str(input("Enter your Name:"))
        self.type=str(input("Type of account:"))
        print("Your account no:", self.acno)
        print("Your name:", self.name)
        print("Type of account:", self.type)
        print("Account Created")

    def deposit(self):
        amount=int(input("Enter the amount to deposit:"))
        self.balance+=amount
        print("Your New Balance ", self.balance)

    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        if(amount>self.balance):
             print("Insufficient Balance!")
        else:
             self.balance-=amount
             print("Your Remaining Balance " ,self.balance)

    def enquiry(self):
        print("Your Balance ", self.balance)

account = Account()
account.create()
account.deposit()
account.withdraw()
account.enquiry()