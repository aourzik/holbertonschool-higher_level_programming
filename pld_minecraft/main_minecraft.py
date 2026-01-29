#!/usr/bin/python3

from minecraft import Character, Animals, Monster

character1= Character("Bobby", 20, 10, 5, 2, 2, 2)
monster1= Monster("Zombie", 10, 5, 2, 0, 1, 2)

print("PV de", character1.get_name(), ":",character1.get_health(), "/ PV de", monster1.get_name(), ":", monster1.get_health(), "\n")
print(character1.get_name(), " tombe sur ", monster1.get_name(), " et lui propose un combat !")
character1.attack_action(monster1)
print("\nCOMBAT")
print(character1.get_name(), " a attaqué", monster1.get_name(), " et maintenant", monster1.get_name(), " a ", monster1.get_health(), " PV.")
monster1.attack_action(character1)
print(monster1.get_name(), " a attaqué", character1.get_name(), " et maintenant", character1.get_name(), " a ", character1.get_health(), " PV.")
character1.attack_action(monster1)
print(character1.get_name(), " a attaqué", monster1.get_name(), " et maintenant", monster1.get_name(), " a ", monster1.get_health(), " PV. Le monstre est MORT !")
print("\nAprès ce combat,", character1.get_name(), "a besoin de se soigner parce qu'il a été légèrement blessé par", monster1.get_name(), ".")
character1.get_heal(character1.heal)
print("Maintenant,", character1.get_name(), "dispose à nouveau de", character1.get_health(), "PV.")