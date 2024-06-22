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