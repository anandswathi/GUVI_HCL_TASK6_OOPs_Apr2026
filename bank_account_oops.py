"""
Python Task-6

Problem 1: Bank Account

Create a base class BankAccount with attributes like account_number, balance, and methods like
deposit() and withdraw(). Inherit from this class to create subclasses SavingsAccount and
CurrentAccount. The SavingsAccount should have an interest rate and a method to calculate interest.
The CurrentAccount should have a minimum balance requirement.

Implement encapsulation to protect the account balance and ensure that withdrawals cannot exceed
the balance or minimum balance requirements.
"""

# Base Class BankAccount
class BankAccount:

    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.__balance = float(balance) # Private data member -> Encapsulation implemented

    # Get method for balance
    def get_balance(self):
        return self.__balance

    # Set method(Protected method) to update balance internally
    def _set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):

        if amount > 0.0:
            self.__balance += float(amount)
            print("Deposited Amount: Rs.{}".format(amount))
            print("New Balance: Rs.{}".format(self.__balance))
        else:
            print("Deposit Amount must be positive.")

    def withdraw(self, amount):

        if amount > 0.0 and amount < self.__balance:
            self.__balance -= float(amount)
            print("Amount Withdrawn: Rs.{}".format(amount))
            print("New Balance: Rs.{}".format(self.__balance))
        else:
            if amount > self.__balance:
                print("Withdrawal denied. Insufficient Balance.")
            elif amount < 0.0:
                print("Withdrawal denied. Invalid Amount.")

# Class SavingsAccount inheriting from Base Class BankAccount
class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100 # Interest calculation
        print("Calculated Interest: {}".format(interest))
        return interest

# Class CurrentAccount inheriting from Base Class BankAccount
class CurrentAccount(BankAccount):

    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = float(minimum_balance)

    def withdraw(self, amount):

        if amount > 0.0 and (self.get_balance() - amount) >= self.minimum_balance:
            new_balance = float(self.get_balance() - amount)
            self._set_balance(new_balance)
            print("Amount Withdrawn: Rs.{}".format(amount))
            print("New balance: Rs.{}".format(new_balance))

        else:
            if (self.get_balance() - amount) >= self.minimum_balance:
                print("Withdrawal denied. Insufficient Balance.")
            elif amount < 0.0:
                print("Withdrawal denied. Invalid Amount.")


# Example usage
print("\n----------Account type: SAVINGS ACCOUNT----------")
savings = SavingsAccount("SBI100123", 1500, 2.50)
savings.deposit(10000)
savings.deposit(-1000) # will fail due to negative amount
savings.withdraw(2000) # valid withdrawal
savings.calculate_interest()

print()

print("----------Account Type: CURRENT ACCOUNT----------")
current = CurrentAccount("SBI100456", 2000, 500)
current.deposit(850)
current.withdraw(-1500) # will fail due to invalid amount
current.withdraw(2800)  # will fail due to minimum balance
current.withdraw(1600)  # valid withdrawal
