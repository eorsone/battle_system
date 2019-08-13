from random import randint

class Status_Effect():
    def __init__(self, name):
        self.name = name
        
    def __str__():
        return self.name

    def apply(self, character):
        pass

class Defend(Status_Effect):
    def __init__(self):
        super().__init__('defend')
        self.duration = 1

    def apply_turn_start(self, character):
        self.duration -= 1
        if self.duration <= 0:
            character.status_effects.remove(self)
            character.bonus_defense -= 2
            print('defend removed\n')

    def apply(self, character):
        print(f'{self.name} applied')
        character.bonus_defense += 2
    
class Character():
    def __init__(self, name, hp=10, attack=5, defense=2, agility=3):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = 2
        self.agility = agility
        self.status = 'alive'
        self.bonus_attack = 0
        self.bonus_defense = 0
        self.status_effects = []

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
    for status_effect in attacker.status_effects:
        status_effect.apply(attacker)
    for status_effect in target.status_effects:
        status_effect.apply(target)

    damage = bound_zero((attacker.attack+randint(1,4)+attacker.bonus_attack) - (target.defense+target.bonus_defense))
    target.hp -= damage
    print(f'{attacker.name} dealt {damage} damage to {target.name}\n')
    wait_confirmation()
    if target.hp <= 0:
        target.status = 'dead'
        print(f'{target.name} is dead.')

def defend(defender):
    print(f'{defender.name} used defend')
    wait_confirmation()
    defender.status_effects.append(Defend())

def execute_command(command):
    global player, enemy
    if command == '1':
        attack(player, enemy)
    elif command == '2':
        defend(player)
    else:
        print("\nInvalid Input\n")

def run_enemy_turn(enemy):
    global player
    if enemy.status == 'alive':
        attack(enemy, player)

def wait_confirmation():
    input()

def update_state():
    global player, enemy, isRunning
    if player.status == 'dead':
        print('Game Over')
        isRunning = False
    elif enemy.status == 'dead':
        print('Congratulations you won')
        isRunning = False

def apply_turn_start_effects(player, enemy):
    for status_effect in player.status_effects:
        status_effect.apply_turn_start(player)

    for status_effect in enemy.status_effects:
        status_effect.apply_turn_start(enemy)   

def main():
    global player, enemy
    player = Character('Player',10, 5)
    enemy = Character('Benz',10, 3)
    while isRunning:
        apply_turn_start_effects(player, enemy)
        display_status(player)
        display_menu()
        command = getInput()
        execute_command(command)
        run_enemy_turn(enemy)
        update_state()

if __name__ == "__main__":
    main()