# OOP Task 
# 1.Create a class called BankAccount with the following attributes: 
# -account number -balance -owner name -date opened
# 2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info() 
# 3.Create 2 BankAccount objects that can deposit, withdraw and display_info


class BankAccount:
    def __init__(self, account_number, owner_name, balance, date_opened):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.date_opened = date_opened

    # deposit

    def deposit(self, amount):
        self.balance += amount

    # withdraw

    def withdraw(self, amount):
        self.balance -= amount
           

    # display

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")

    # create two accounts

client1 = BankAccount("1001","Peter", 10000, "2025-12-02")
client2 = BankAccount("1002","Alice", 30000, "2025-12-01")

client1.deposit(1500)

client1.display_info()
# client2.display_info()



