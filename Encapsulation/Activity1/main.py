from bank_account import *
thisguy =  BankAccount(777777, 80, "Ario")
thatguy = BankAccount(123456, 16, "Jamie")

thisguy.set_accountNumber(897979)
print(thisguy.get_accountNumber())
thisguy.set_balance(4)
print(thisguy.get_balance())
thisguy.set_ownerName("Wario")
print(thisguy.get_ownerName())
thisguy.deposit(150)
print(thisguy.get_balance())
thisguy.withdraw(4)
print(thisguy.get_balance())



thatguy.set_accountNumber(444444)
print(thatguy.get_accountNumber())
thatguy.set_balance(0)
print(thatguy.get_balance())
thatguy.set_ownerName("Ginger")
print(thatguy.get_ownerName())
thatguy.deposit(10000000000000000000000000000000000000000000000000000000000000000000000000000000000)
print(thatguy.get_balance())
thatguy.withdraw(1)
print(thatguy.get_balance())
