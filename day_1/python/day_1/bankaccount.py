class InsufficientFundsError(Exception):
    pass

class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError(f'Entered amount of {amount} is wrong')
        self.balance += amount
        return self.balance
    # try:
    #     deposit(amount)
    # except ValueError as v:
    #     print('Transcation failed{v}')

    def withdraw(self,amount):
        if amount <= 0: 
            raise ValueError(f'Entered amount of {amount} is wrong')
        elif amount > self.balance:
            raise InsufficientFundsError(f'Cannot withdraw {amount}')
        self.balance -= amount
        return self.balance
    # try: 
    #     withdraw(amount)
    # except InsufficientFundsError as e:
    #     print('Insufficient balance')

assert issubclass(InsufficientFundsError, Exception)

acc = BankAccount("Divya")
assert acc.owner == "Divya"
assert acc.balance == 0
assert acc.deposit(100) == 100
assert acc.withdraw(30) == 70
assert acc.balance == 70

acc2 = BankAccount("Asha", 50)
assert acc2.balance == 50

# Withdrawing too much
try:
    acc.withdraw(500)
    assert False, "Expected InsufficientFundsError"
except InsufficientFundsError:
    pass
assert acc.balance == 70

# Invalid amounts
for bad in [0, -10]:
    try:
        acc.deposit(bad)
        assert False, "Expected ValueError on deposit"
    except ValueError:
        pass
    try:
        acc.withdraw(bad)
        assert False, "Expected ValueError on withdraw"
    except ValueError:
        pass
assert acc.balance == 70

# Exact balance
assert acc.withdraw(70) == 0

print("All tests passed!")