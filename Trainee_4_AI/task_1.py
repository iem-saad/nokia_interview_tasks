#*******************************************************
# NOKIA INTERVIEW TASK 1 CODE                          *
#                                                      *
# Author: Saad Abdullah                                *
# E-mail: iem.saad@hotmail.com                         *
# Created: 29 APR 2025                                 *
# Last modification: 29 APR 2025                       *
# Lint Score: 10/10 Using Pylint                       *
#******************************************************/

"""
This code implements a simple bank account class with basic functionalities such as 
deposit, withdraw, and get account information.
"""

class BankAccount:
    """
    Represents a generic bank account.
    """

    def __init__(self, account_number: str, account_holder_name: str, balance: float = 0.0) -> None:
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        # Intentionally made it private to prevent direct access in future.
        self.__balance = balance

    @property
    def balance(self) -> float:
        """Safely get balance."""
        # Made this instead of get_balance().
        return self.__balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"\nDeposited {amount}. New balance: {self.__balance:.2f}")
        else:
            print("\nDeposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        """Withdraw money if sufficient balance exists."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"\nWithdrew {amount}. New balance: {self.__balance:.2f}")
        else:
            print("\nWithdrawal amount must be positive and within available balance.")

    def get_account_info(self) -> None:
        """Display the account details."""
        print(f"\nAccount [{self.account_number}] Balance: {self.__balance:.2f}")

if __name__ == "__main__":
    print("*****************************************************")
    print("\n****************** WELCOME **************************")
    print("\n-------------- Creating a Bank Account --------------")
    account = BankAccount("123456789", "Saad Abdullah", 1000.0)
    account.get_account_info()
    account.deposit(500)
    account.withdraw(200)
    account.get_account_info()
    print("\nTrying to widthdraw more than the balance:")
    account.withdraw(2000)  # Attempt to withdraw more than the balance
    account.deposit(-100)  # Attempt to deposit a negative amount
    print(f"\nEnding Balance: {account.balance:.2f}")  # Accessing the balance property
    print("\n----------------- End of Program -------------------")
    print("*******************************************************")
