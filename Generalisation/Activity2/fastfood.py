import random
class Employee():
    def __init__(self, name, Id, hourlyWage, shiftHours:int, currentBalance):
        self._name = name
        self._Id = Id
        self._hourlyWage = hourlyWage
        self._shiftHours = shiftHours
        self._currentBalance = currentBalance
    
    def clockIn(self):
        hours = int(input("how long is your shift in hours? "))
        self._shiftHours = self._shiftHours + hours
        print("welcome!")
    
    def clockOut(self):
        return f"you have worked {self._shiftHours} this week and will recieve ${self._shiftHours * self._hourlyWage}"

    def get_pay(self):
        money = self._shiftHours * self._hourlyWage
        self._currentBalance = self._currentBalance + money
        print(f"You recieved ${money}, your current balance is now ${self._currentBalance}")
        self._shiftHours = 0

class Manager(Employee):
    def __init__(self, name, Id, hourlyWage, shiftHours, currentBalance, niceness:int):
        super().__init__(name, Id, hourlyWage, shiftHours, currentBalance)
        self._niceness = niceness
    
    def gun(self):
        if self._niceness < 50:
            return "gun fired, employee killed"
        
        else:
            return "gun unloaded"

class TeamMember(Employee):
    def __init__(self, name, Id, hourlyWage, shiftHours, currentBalance, casual:bool):
        super().__init__(name, Id, hourlyWage, shiftHours, currentBalance)
        self._casual = casual
    
    def Casual(self):
        if self._casual == True:
            self._hourlyWage = self._hourlyWage * 1.1
        
        else:
            self._hourlyWage = self._hourlyWage

class Barista(TeamMember):
    def __init__(self, name, Id, hourlyWage, shiftHours, currentBalance, casual, skill:int):
        super().__init__(name, Id, hourlyWage, shiftHours, currentBalance, casual)
        self._skill = skill
    
    def makeCoffee(self):
        coffees = random.randint(0,8)
        tip = 0
        while coffees > 0:
            self._skill = self._skill + 5
            coffeeQuality = random.randint(self._skill - 10 ,self._skill + 10)
            coffees = coffees - 1
            if coffeeQuality < 20:
                print("This coffee is disgusting!")

            if 25 <= coffeeQuality < 50:
                print("This coffee is alright")
                tip = tip + 2
             
            if 50 <= coffeeQuality < 75:
                print("This coffee is pretty good")
                tip = tip + 5
            
            if 75 <= coffeeQuality < 100:
                print("This coffee is pretty great")
                tip = tip + 10

        self._currentBalance = self._currentBalance + tip
        return f"You made ${tip}, your balance is now ${self._currentBalance}"

class AverageJoe(TeamMember):
    def __init__(self, name, Id, hourlyWage, shiftHours, currentBalance, casual, lazy:bool):
        super().__init__(name, Id, hourlyWage, shiftHours, currentBalance, casual)
        self._lazy = lazy
    
    def fired(self):
        if self._lazy:
            return"you're fired!"
        else:
            return "you're safe... for now"