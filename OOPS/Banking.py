class Bank:
    def create(self, name, adhar, address, balance):
        self.name = name 
        self.adhar = adhar
        self.address = address
        self.account = 1220000012
        self.balance = balance
    def showDetils(self):
        print(f"Name: {self.name}\nAccount:{self.account}\naddress:{self.address}")
    def deposite(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Balance.")
        else:
            self.balance -=amount
            checker = input("Do you want to see your balance(Enter y): ")
            if checker == 'y':
                self.showBalance()
            
    def showBalance(self):
        print("Your Balance is: ", self.balance)
    
c1 = Bank()
c1.create("Jeeban", 125123214562, "Siadimal", 1100)
c1.showDetils()
c1.withdraw(100)