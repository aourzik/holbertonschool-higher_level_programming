#!/usr/bin/python3

class Character:
    def __init__(self, name, health, xp, attack, heal, movement):
        self.name = name
        self.health = health
        self.xp = xp
        self.attack = attack
        self.heal = heal
        self.movement = movement

class Animals(Character):
    def __init__(self, type, health, movement):
        super().__init__(health, movement)
        self.type = type


class Monster(Character):
    def __init__(self, type, health, xp, attack, movement):
        super().__init__(health, xp, attack, movement)
        self.type = type

