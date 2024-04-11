class Account:
    def __init__(self, name, balance):
        self.__name = name         # private attribute
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

# Creating an instance
acc = Account("John", 100)

# Accessing the private variable (this will fail)
# print(acc.__balance)

# Using the getter method
print(acc.get_balance())  # Output: 100

# Using the public method to modify the private variable
acc.deposit(50)
print(acc.get_balance())  # Output: 150
