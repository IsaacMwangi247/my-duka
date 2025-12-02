# OOP Task 
# 1.Create a class called BankAccount with the following attributes: 
# -account number -balance -owner name -date opened
# 2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info() 
# 3.Create 2 BankAccount objects that can deposit, withdraw and display_info


from datetime import datetime

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.date_opened = datetime.now().strftime("%Y-%m-%d")  # auto-set date

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

    def display_info(self):
        print("\n--- Bank Account Information ---")
        print(f"Owner Name:    {self.owner_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance:        {self.balance}")
        print(f"Date Opened:    {self.date_opened}")
        print("--------------------------------\n")


# --------------------------
# CREATE 2 ACCOUNT OBJECTS
# --------------------------

account1 = BankAccount("ACC001", "Tala", 50000)
account2 = BankAccount("ACC002", "Tatu", 10000)

# Testing actions
account1.deposit(2000)
account1.withdraw(1500)
account1.display_info()

account2.deposit(500)
account2.withdraw(12000)  
account2.display_info()