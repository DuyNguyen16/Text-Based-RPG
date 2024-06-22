class Character:
  def __init__(self, name, health, attack_power, defense):
    self.name = name
    self.health = health
    self.attack_power = attack_power
    self.defense = defense
    self.inventory = []

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


class Item:
  def __init__(self, name, effect):
    self.name = name
    self.effect = effect

  def apply_effect(self, character):
    self.effect(character)


def health_potion_effect(character):
    character.health += 20
    print(f"{character.name}'s health is restored by 20 points.")

def strength_potion_effect(character):
      character.attack_power += 5
      print(f"{character.name}'s attack power is increased by 5 points temporarily.")

health_potion = Item("Health Potion", health_potion_effect)
strength_potion = Item("Strength Potion", strength_potion_effect)
    
def battle():
    hero = Character("Hero", 100, 20, 5)
    monster = Character("Monster", 80, 15, 3)
    
    hero.pick_up_item(health_potion)
    hero.pick_up_item(strength_potion)

    hero.use_item(strength_potion)
    
    print(hero.attack_power)

battle()
