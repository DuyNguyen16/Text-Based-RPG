import os


class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.inventory = []
        self.weapon = []
        self.gold = 100
        self.turn = False

    # attack
    def attack(self, target):
        damage = self.attack_power - target.defense
        if damage > 0:
            target.take_damage(damage)
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} but it's ineffective.")

    # taken damage
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")

    # Picking up item
    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name} Bought a {item.name}.")

    def use_item(self, item):
        if item in self.inventory:
            item.apply_effect(self)
            self.inventory.remove(item)
            print(f"{self.name} used {item.name}.")
        else:
            print(f"{self.name} doesn't have {item.name}.")


# ========================================================================
class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply_effect(self, character):
        self.effect(character)


# ========================================================================
def defense_potion_effect(character):
    character.health += 2


def health_potion_effect(character):
    character.health += 20
    print(f"{character.name}'s health is restored by 20 points.")


def strength_potion_effect(character):
    character.attack_power += 5
    print(f"{character.name}'s attack power is increased by 5 points temporarily.")


def sword_bonus(character):
    character.attack_power += 10
    print(f"{character.name} equipped a sword and gain 10 attack power")


defense_potion = Item("Defense Potion", defense_potion_effect)
health_potion = Item("Health Potion", health_potion_effect)
strength_potion = Item("Strength Potion", strength_potion_effect)
sword = Item("Sword", sword_bonus)
# ========================================================================


def open_shop(player):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Item Shop")
        print("--------------------------------------------------------------")
        print(f"{player.name} have {player.gold} golds")
        print("--------------------------------------------------------------")
        print(
            f"1. Sword (40 gold) x{player.inventory.count(sword)}\n2. Health Boost Potion (20 gold) x{player.inventory.count(health_potion)}\n3. Strength Boost Potion (20 gold) x{player.inventory.count(strength_potion)}\n4. Defense Boost Potion (20 gold) x{player.inventory.count(defense_potion)}\n5. Go Back"
        )
        print("--------------------------------------------------------------")
        player_action = int(input("Buy an Item: "))

        match player_action:
            case 1:
                if player.gold < 40:
                    continue
                player.add_item_to_inventory(sword)
                player.gold -= 40
            case 2:
                if player.gold < 20:
                    continue
                player.add_item_to_inventory(health_potion)
                player.gold -= 20
            case 3:
                if player.gold < 20:
                    continue
                player.add_item_to_inventory(strength_potion)
                player.gold -= 20
            case 4:
                if player.gold < 20:
                    continue
                player.add_item_to_inventory(defense_potion)
                player.gold -= 20
            case 5:
                break


def open_inventory(player):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{player.name}'s Inventory")
        print("--------------------------------------------------------------")
        print(f"Number of Items: {len(player.inventory)}")
        print("--------------------------------------------------------------")
        for i in range(len(player.inventory)):
            print(
                f"{i + 1}. {player.inventory[i].name} x{player.inventory.count(player.inventory[i])}"
            )
        print(f"{len(player.inventory) + 1}. Go Back")
        print("--------------------------------------------------------------")
        item_select = int(input(f"Select an item to use (1-5): ")) - 1
        if (item_select > len(player.inventory)):
          continue
        else:
          match item_select:
              case 0:
                  if (len(player.inventory) == 0):
                    break
                  if player.inventory[0] not in player.inventory:
                      continue
                  player.use_item(player.inventory[0])
                  print("--------------------------------------------------------------")
                  next_action = input("Contiue? (y or n): ")
                  print("--------------------------------------------------------------")
              case 1:
                  if (len(player.inventory) == 1):
                    break
                  if player.inventory[1] not in player.inventory:
                      continue
                  player.use_item(player.inventory[1])
                  print("--------------------------------------------------------------")
                  next_action = input("Contiue? (y or n): ")
                  print("--------------------------------------------------------------")
              case 2:
                  if (len(player.inventory) == 2):
                    break
                  if player.inventory[2] not in player.inventory:
                      continue
                  player.use_item(player.inventory[2])
                  print("--------------------------------------------------------------")
                  next_action = input("Contiue? (y or n): ")
                  print("--------------------------------------------------------------")
              case 3:
                  if (len(player.inventory) == 3):
                    break
                  if player.inventory[3] not in player.inventory:
                      continue
                  player.use_item(player.inventory[3])
                  print("--------------------------------------------------------------")
                  next_action = input("Contiue? (y or n): ")
                  print("--------------------------------------------------------------")
              case 4:
                  break


def player_turn(current_player, other_player):
    while current_player.turn == True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{current_player.name}'s turn!")
        print("--------------------------------------------------------------")
        print("Player Stats")
        print("--------------------------------------------------------------")
        print(f"Health: {current_player.health}")
        print(f"Attack Power: {current_player.attack_power}")
        print(f"Defense: {current_player.defense}")
        print("--------------------------------------------------------------")
        current_player_action = int(
            input("1. Shop\n2. Inventory\n3. Attack\nPlease select an action (1-3): ")
        )
        # Player 1 turn
        if current_player_action == 1:
            open_shop(current_player)
        elif current_player_action == 2:
            open_inventory(current_player)
        elif current_player_action == 3:
            current_player.attack(other_player)


def battle():
    player1 = Character("Player1", 100, 20, 5)
    player2 = Character("Player2", 100, 20, 5)

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        first_move = int(input("Select a player to go first (1 or 2): "))
        if first_move == 1:
            player1.turn = True
            break
        elif first_move == 2:
            player2.turn = True
            break

    while player1.health > 0 or player2.health > 0:
        if player1.turn:
            player_turn(player1, player2)
        else:
            player_turn(player2, player1)


battle()
