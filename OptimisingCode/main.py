def add(x,y):
    return x + y

print(add(5,7))

print("Welcome, Ali!\n"
"Welcome, Ben!\n"
"Welcome, Cat!\n"
"Welcome, Doge!\n"
"Welcome, Eggbert!\n"
"Welcome, Fred!\n"
"Welcome, Grod!\n")


class Animal:
    def __init__(self):
        self.sound = ""

    def make_sound(self):
        if self.sound == "woof":
            print("Dog goes woof")
        elif self.sound == "meow":
            print("Cat goes meow")
        elif self.sound == "moo":
            print("Cow goes moo")
        else:
            print("Unknown animal sound")

class Dog(Animal):
    def __init__(self):
        self.sound = "woof"

class Cat(Animal):
    def __init__(self):
        self.sound = "meow"

class Cow(Animal):
    def __init__(self):
        self.sound = "moo"


animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.make_sound() # I am confused by this one.

words = ["hello", "world", "!"]
sentence = " ".join

print(sentence.strip())

fruit_stock = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruit_stock):
    print(i, fruit)
