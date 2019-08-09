class Character():
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = 5

isRunning = True

def getInput():
    return input("Pick A Option\n")

def display_menu():
    print("Your Move")
    print("1.Attack")
    print("2.Defend\n")

def display_status(character):
    print(f'{character.name} HP is: {character.hp}')

def bound_zero(number):
    if number < 0:
        return 0
    return number

def attack(attacker, target):
    damage = bound_zero(attacker.attack - target.defense)
    target.hp -= damage
    print(f'{attacker.name} dealt {damage} damage to {target.name}\n')

def execute_command(command):
    global player, enemy
    if command == '1':
        attack(player, enemy)
    elif command == '2':
        print("\nDefend\n")
    else:
        print("\nInvalid Input\n")
        
def main():
    global player, enemy
    player = Character('Player',10, 4)
    enemy = Character('Benz',10, 4)
    while isRunning:
        display_status(player)
        display_menu()
        command = getInput()
        execute_command(command)



if __name__ == "__main__":
    main()