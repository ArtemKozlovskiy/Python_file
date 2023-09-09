from unit import Unit


swordsman = Unit("Мечник", hp=100, attack=15, defense=8, critical_damage_multiplier=2.2, critical_chance=0.3)
archer = Unit("Лучник", hp=90, attack=20, defense=4, critical_damage_multiplier=2.0, critical_chance=0.25)
mage = Unit("Маг", hp=80, attack=25, defense=10, critical_damage_multiplier=2.5, critical_chance=0.4)

print("Характеристики юнітів")
print(swordsman.get_info())
print(archer.get_info())
print(mage.get_info())
print('   ')

swordsman.attack_enemy(archer)
archer.attack_enemy(mage)
mage.attack_enemy(swordsman)

print("Характеристики юнітів після бою")
print(swordsman.get_info())
print(archer.get_info())
print(mage.get_info())

if swordsman > archer and swordsman > mage:
    print("Мечник найсильніший")
elif archer > swordsman and archer > mage:
    print("Лучник найсильніший")
elif mage > swordsman and mage > archer:
    print("Маг найсильніший")
else:
    print("Нічия")