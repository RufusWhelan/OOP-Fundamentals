from GameObjects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
playerCharacter = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

# TODO: Create an instance of Weapon with random damage between 12 and 15
playerWeapom = Weapon('Master Sword', 'sword', random.randint(12,15), 0.95)

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
playerEnemy = Enemy("")

# Print the player character details
print(f"Player Name: {playerCharacter.name}")
print(f"Player Race: {playerCharacter.race}")
print(f"Player Class: {playerCharacter.cls}")
print(f"Player Attack: {playerCharacter.atk}")
print(f"Player Health: {playerCharacter.health}")

# TODO: Print the player weapon details
print(f"Weapon Name: {playerWeapom.name}")
print(f"Weapon type: {playerWeapom.category}")
print(f"damage: {playerWeapom.damage}")
print(f"accuracy: {playerWeapom.accuracy}")

# TODO: Print the enemy character details
playerList = [Player('timmy', 'Dwarf', 'Fighter', 3, 180), Player('Gyattatron Prime', 'elf', 'mage', 100, 5), Player('Rufor', 'half-elf', 'bard', 7, 120), Player('Jamie', 'Ranga', 'Ranga', 5, 140)]
weapons = [Weapon("Longsword", "Melee", 50, 80), Weapon("Crossbow", "Ranged", 40, 75), Weapon("Handgun", "Firearm", 60, 85), Weapon("Rocket Launcher", "Explosive", 100, 60)
]

def pickCharacter():
    input(f"Would you like to be {playerList[1].name}, Gyattatron Prime, rufor or jamie? (input: 1,2,3,4)")
    input(f"Would you like to have the longsword, crossbow, handgun or rocket launcher? (input: 1,2,3,4)")

