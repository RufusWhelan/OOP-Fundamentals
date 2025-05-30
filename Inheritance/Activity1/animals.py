class Animal:
    def __init__(self, name):
        self._name = name

    def sound(self):
        return "This animal makes a sound, but it's not defined."


class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self._sound = sound

    def sound(self):
        super().sound()
        return f"The dog named {self._name} says: {self._sound}"


class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self._sound = sound

    def sound(self):
        super().sound()
        return f"The cat named {self._name} says: {self._sound}"

    
