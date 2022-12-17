import json
import random

class Character():
    def __init__(self):
        self.name = "player"
        self.strength = 0
        self.intel = 0
        self.wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.race = ""
        self.char_class = ""
        self.level = 1
        self.hit_point_max = 0
        self.movement = 0
        self.armors = []
        self.weapons = []
        self.xp = 0
        self.type = ""
        self.current_weapon = ""
        self.current_armor = ""
    
    def load_from_json(self, path):
        with open(path) as p:
            character = json.load(p)

        self.name = character.get('name')
        self.strength = character.get('str')
        self.intel = character.get('int')
        self.wisdom = character.get('wis')
        self.dexterity = character.get('dex')
        self.constitution = character.get('con')
        self.charisma = character.get('chr')
        self.race = character.get('race')
        self.char_class = character.get('class')
        self.level = character.get('lvl')
        self.hit_point_max = character.get('hp')
        self.movement = character.get('spd')
        self.xp = character.get('xp')




    def set_current_weapon(self):
        pass
    def roll_to_hit(self):
        pass
    def roll_for_damage(self):
        pass
    def get_ac(self):
        if self.race == "Human":
            return 13
        elif self.race == "Doppelganger":
            return 14
        elif self.race == "Dark Elf":
            return 15
        elif self.race == "Grotesque":
            return 16
        else:
            return 10
    def get_movement(self):
        pass
    def get__ability_bonuses(self):
        pass