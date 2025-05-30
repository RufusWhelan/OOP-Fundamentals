from fastfood import *

john = Manager("john", 4, 22.50, 36, 1000, 80)
john.clockIn()
print(john.clockOut())
john.get_pay()
print(john.gun())

kevin = TeamMember("Kevin", 2, 15.00, 20, 300, True)
kevin.Casual()
kevin.clockIn()
print(kevin.clockOut())
kevin.get_pay()

lisa = Barista("Lisa", 3, 14.00, 10, 200, True, 50)
lisa.Casual()
lisa.clockIn()
print(lisa.makeCoffee())
print(lisa.clockOut())
lisa.get_pay()

tom = AverageJoe("Tom", 4, 13.00, 15, 150, False, True)
tom.Casual()
tom.clockIn()
print(tom.clockOut())
tom.get_pay()
print(tom.fired())