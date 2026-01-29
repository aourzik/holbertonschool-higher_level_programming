#!/usr/bin/python3

class Character:
    def __init__(self, name, health, xp, attack, heal, movement, damage):
        self.name = name
        self.health = health
        self.xp = xp
        self.attack = attack
        self.heal = heal
        self.movement = movement
        self.damage = damage

    def get_name(self):
        return self.name
    
    def get_health(self):
        return self.health
    
    def get_xp(self):
        return self.xp
    
    def get_movement(self):
        return self.movement
    
    def damages(self, damage):
        self.health -= damage
    
    def attack_action(self, target):
        target.damages(self.attack)

class Animals(Character):
    def __init__(self, name, health, movement):
        super().__init__(name, health, movement)


class Monster(Character):
    def __init__(self, name, health, xp, attack, heal, movement, damage):
        super().__init__(name, health, xp, attack, heal, movement, damage)
