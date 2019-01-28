class Account():
    balance = 0.00
    def __init__ (self,name):
        self.name = name
    
    def get_balance (self):
        return self.balance

    def get_name(self):
        return self.name
    
    def deposit(self,amount):
        self.balance += amount
        print("Deposit of {} was successfull".format(amount))

    def withdraw(self, amount):
        self.balance -=amount
        print("Widthdrawal of {} was successfull".format(amount))


    def change_name(self,name):
        self.name = name

    def transfer(self,amount,customer):
        customer.account.deposit(amount)
        self.balance -=amount
        print("Transfer of {} to {} was successfull".format(amount,customer))

class Customer():

    def __init__ (self,name,age,account):
        """
        name, age, account
        """
        self.name = name
        self.age = age
        self.account = account
    
    def get_name (self):
        return self.name
    
    def get_age (self):
        return self.age
    
    def change_name(self,name):
        self.name = name
    
    def __str__ (self):
        return self.name

# myAcc = Account(name="Savings")
myAcc2 = Account(name="Savings")

# customer1 = Customer("Samfield Hawb Bassey",23,myAcc)
customer1 = Customer("Samfield Hawb Bassey",23,Account(name="Saving"))
customer2 = Customer("Enoobong Hawb Bassey",27,myAcc2)

print(customer1.account.get_balance())
customer1.account.deposit(50000)
print('New balance')
print(customer1.account.get_balance())

customer1.account.transfer(5000,customer2)
print(customer1.account.get_balance())
print('Customer {} new balance'.format(customer2))
print(customer2.account.get_balance())
customer1.account.withdraw(3000)


print('Customer {} new balance'.format(customer1))
print(customer2.account.get_balance())
