class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name      # Store the player's name
        self.race = race      # Store the player's race (e.g., human, elf, etc.)
        self.cls = cls        # Store the player's class (e.g., warrior, mage, etc.)
        self.atk = atk        # Store the player's attack power
        self.health = health  # Store the player's health points

class Weapon:
    def __init__(self, name, category, damage, accuracy):
        self.name = name
        self.category = category
        self.damage = damage
        self.accuracy = accuracy
# TODO: Create an 'Enemy' class.
class Enemy:
    def __init__(self, name, race, damage, health):
        self.name = name
        self.race = race
        self.damage = damage
        self.heath = health
    

