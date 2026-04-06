# TamaraSamokhvalova_ProgrammingExercise_9

class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
# set up the account information
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Deposit money into account
    def deposit(self, amount_to_add):
        if amount_to_add > 0:
            self.amount += amount_to_add
        else:
            print("Deposit must be greater than 0")

    # Withdraw money from the account
    def withdraw(self, amount_to_take):
        # Check if there is enough money
        if amount_to_take > 0 and amount_to_take <= self.amount:
            self.amount -= amount_to_take
        else:
            print("Invalid withdrawal amount")

    # Change interest rate
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Get current balance
    def get_balance(self):
        return self.amount

    # Calculate interest based on days
    def calculate_interest(self, days):
        # Simple interest formula:
        # interest = balance * rate * (days / 365)
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    # Print account information nicely
    def __str__(self):
        return (
            f"\nAccount Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount:.2f}\n"
            f"Interest Rate: {self.interest_rate * 100:.2f}%\n"
        )


def test_bank_account():

    # Create a bank account object
    account = BankAcct("Tamara", "123456", 1000, 0.05)

    # Print starting account info
    print("Starting Account Info:")
    print(account)

    # Deposit money
    account.deposit(500)
    print("After depositing $500:")
    print(account)

    # Withdraw money
    account.withdraw(200)
    print("After withdrawing $200:")
    print(account)

    # Change interest rate
    account.adjust_interest_rate(0.07)
    print("After changing interest rate to 7%:")
    print(account)

    # Show balance
    print("Current Balance:", account.get_balance())

    # Calculate interest for 30 days
    interest = account.calculate_interest(30)
    print("Interest for 30 days: $", round(interest, 2))


if __name__ == "__main__":
    test_bank_account()