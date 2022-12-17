import json

class Armor():
    def __init__(self):
        self.name = 'No Armor'
        self.price = 0
        self.weight = 0
        self.ac = 0
     
def load(self, path):    
        with open(path) as f:
            armor = json.load(f)

        print(armor)
        self.name = armor.get("name")
        self.price = armor.get("price")
        self.weight = armor.get("weight")
        self.ac = armor.get("ac")