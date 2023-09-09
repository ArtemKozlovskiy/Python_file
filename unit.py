import random


class Unit:
    def __init__(self, unit_type, hp, attack, defense, critical_damage_multiplier, critical_chance):
        self.unit_type = unit_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.critical_damage_multiplier = critical_damage_multiplier
        self.critical_chance = critical_chance

    def get_info(self):
        return f"{self.unit_type} - HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, " \
               f"Critical Damage Multiplier: {self.critical_damage_multiplier}, " \
               f"Critical Chance: {self.critical_chance}"

    def __str__(self):
        return self.get_info()

    def __gt__(self, other):
        return self.hp > other.hp

    def __lt__(self, other):
        return self.hp < other.hp

    def __eq__(self, other):
        return self.hp == other.hp

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0

        if random.random() < self.critical_chance:
            damage *= self.critical_damage_multiplier

        enemy.hp -= damage
        if enemy.hp < 0:
            enemy.hp = 0
