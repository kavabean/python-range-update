from rpg.character import Character
import random

class Generator():
    def __init__(self):
        self.random_nums = []


    def character(self):
        char = Character()
        char.hit_point_max = 6
        char.strength = self.rolling()
        char.intel = self.rolling()
        char.wisdom = self.rolling()
        char.dexterity = self.rolling()
        char.constitution = self.rolling()
        char.charisma = self.rolling()

        return char


    def rolling(self):
        for x in range(4):
            self.random_nums.append(random.randint(1,6))
        self.random_nums.remove(min(self.random_nums))
        summ = sum(self.random_nums)
        self.random_nums = []
        return summ
        