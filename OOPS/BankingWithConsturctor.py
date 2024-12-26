import random as rn

class Bank:
    def __init__(self,name,address,phone,balance):
        self.name = name
        self.address = address
        self.phone = phone
        self.account_no = 1000000112
        self.balance = balance
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance.")
        else:
            self.balance -= amount
    def deposite(self, amount):
        self.balance += amount
    def showBalance(self):
        print("Your Balance is: ",self.balance)
    def showDetails(self):
        print(f"Name: {self.name} \nAccount No:{self.account_no} \nAddress: {self.address}\nPhone:{self.phone} ")


cus1 = Bank("Jeebanjyoti", "Siadimal", "6371317325",200)

cus1.showBalance()