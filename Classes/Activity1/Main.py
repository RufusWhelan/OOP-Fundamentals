from GameObjects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
playerCharacter = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

# TODO: Create an instance of Weapon with random damage between 12 and 15
playerWeapom = Weapon('Master Sword', 'sword', random.randint(12,15), 0.95)

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
playerEnemy = Enemy("peter", "griffin", random.randint(12,15), random.randint(80, 140))

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
weapons = [Weapon("Longsword", "Melee", 50, 80), Weapon("Crossbow", "Ranged", 40, 75), Weapon("Handgun", "gun", 60, 85), Weapon("Rocket Launcher", "Explosive", 100, 60)
]

def pickCharacter():
    playerChoice = 0
    weaponChoice = 0
    while (playerChoice <= 1 or playerChoice >= 4) and (weaponChoice <= 1 or weaponChoice >= 4):
        try:
            playerChoice = int(input(f"Would you like to be {playerList[0].name}, {playerList[1].name}, {playerList[2].name} or {playerList[3].name}? (input: 1,2,3,4) "))
            weaponChoice = int(input(f"Would you like to have the {weapons[0].name}, {weapons[1].name}, {weapons[2].name} or {weapons[3].name}? (input: 1,2,3,4) "))
            if playerChoice <= 1 or playerChoice >= 4 or weaponChoice <= 1 or weaponChoice >= 4:
                print("please enter a valid number (1,2,3,4)")
        except:
            print("please enter an integer")
    print(f"you have selected {playerList[playerChoice - 1].name}")
    return(f"you have selected {weapons[weaponChoice -  1].name} it is {weapons[weaponChoice - 1].category}")

print(pickCharacter())