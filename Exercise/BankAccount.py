# Define Class BankAccount
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = 0.0  # backing attribute
        self.balance = balance  # go through the property setter

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount  # uses property

    def withdraw(self, amount: float):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Invalid withdraw amount.")
        self.balance -= amount


# Test it
acct = BankAccount("Mia", 100)
acct.deposit(50)
acct.withdraw(30)
print(acct.balance)  # ✅ 120
    