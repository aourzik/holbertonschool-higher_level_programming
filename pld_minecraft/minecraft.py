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

class Animals(Character):
    def __init__(self, type, health, movement):
        super().__init__(health, movement)
        self.type = type


class Monster(Character):
    def __init__(self, type, health, xp, attack, movement, damage):
        super().__init__(health, xp, attack, movement,damage)
        self.type = type

