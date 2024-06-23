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
  def pick_up_item(self, item):
    self.inventory.append(item)
    print(f"{self.name} picked up {item.name}.")


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

def open_shop():
  pass

def open_inventory():
  pass

def player_turn(current_player, other_player):
  
  while (current_player.turn == True):
        current_player_action = int(input("1. Shop\n2. Inventory\n3. Attack\nPlease select an action (1-3): "))
        # Player 1 turn
        if (current_player_action == 1):
          open_shop()
        elif (current_player_action == 2):
          open_inventory()
        elif (current_player_action == 3):
          current_player.attack(other_player)
        else:
          print("1. Shop\n2. Inventory\n3. Attack\nPlease select a number between 1-3:")


def battle():
    player1 = Character("Player1", 100, 20, 5)
    player2 = Character("Player2", 100, 20, 5)
    first_move = 0

    while (first_move != 1 or first_move != 2):
      first_move = int(input("Select a player to go first (1 or 2): "))
      if (first_move == 1):
        player1.turn = True
      elif(first_move == 2):
        player2.turn = True
      
    while (player1.health > 0 or player2.health > 0):
      if (player1.turn):
        player_turn(player1, player2)
      else:
        player_turn(player2, player1)





battle()

