class BankAccount:
    def __init__(self, accountNumber, balance, ownerName):
        self._accountNumber = accountNumber
        self._balance = balance
        self._ownerName = ownerName
    
    def get_accountNumber(self):
        return self._accountNumber
    
    def get_balance(self):
        return self._balance
    
    def get_ownerName(self):
        return self._ownerName
    
    def set_accountNumber(self, accountNumber):
        if len(str(accountNumber)) == 6:
            self._accountNumber = accountNumber
        else:
            raise ValueError("Account number must be exactly 6 digits long.")
    def set_balance(self, balance):
        self._balance = balance
    
    def set_ownerName(self, name):
        self._ownerName = name
    
    def deposit(self, amount):
        self._balance = self._balance + amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance = self._balance - amount
        
        else:
            return("You don't have that much money!")