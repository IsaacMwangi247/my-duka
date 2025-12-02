class Person:
    def __init__(self,name,age,height,address,is_married):
        self.name = name
        self.age = age
        self.height = height
        self.address = address
        self.is_married = is_married
    
    def greet(self):
        return f"Hi my name is {self.name}"

person1 = Person("John",65,"170cm","Kimathi Street",False)
person2 = Person("Alvin",20,"178cm","Kimathi St",False)
# print(person1)
print(person1.greet())
print(person1.name)

# OOP Task 
# 1.Create a class called BankAccount with the following attributes: 
# -account number -balance -owner name -date opened
# 2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info() 
# 3.Create 2 BankAccount objects that can deposit, withdraw and display_info

# class BankAccount:
#     def __init__(self,account_number,name,balance,date_created):
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance
#         self.date_created = date_created
#     def greet(self):

