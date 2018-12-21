class bank:
    balance=0
    def deposite(self):
        amt=int(input("enter deposited money :"))
        self.balance+=amt
        print("Your deposite amount is :",self.balance)

    def withdraw(self):
        amt2=int(input("enter withdraw amount :"))
        self.balance-=amt2
        print("after withdraw available balance :", self.balance)
b=bank()
while True:
    ans=input("do you want add more money press y/Y :")
    if ans=="y" or ans=="Y":
        b.deposite()
        b.withdraw()
    else:
        break