class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited {amount}. New balance: {self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew {amount}. New balance: {self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: {self.__account_balance}"

# Create an instance of the BankAccount class
account = BankAccount("123456789","ranjith", 1000)

# Test deposit and withdrawal functionality
print(account.display_balance())  # Display initial balance
print(account.deposit(500))       # Deposit 500
print(account.withdraw(200))      # Withdraw 200
print(account.display_balance())  # Display updated balance
