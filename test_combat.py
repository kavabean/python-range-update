import unittest
from rpg.character import Character

class Test_combat(unittest.TestCase) : 

    def test_character_creation_defaults(self):

        char1 = Character()
        self.assertEqual(char1.name, "player")

    def test_character_creation_from_file(self):
        
        char2 = Character()
        char2.load_from_json('characters/pandora.json')
        self.assertEqual("Pandora", char2.name)

    def test_get_ac(self):

        char = Character()
        self.assertEqual(char.get_ac(), 10)

        char.race = 'Human'
        self.assertEqual(char.get_ac(), 13)

        char.race = 'Doppelganger'
        self.assertEqual(char.get_ac(), 14)

        char.race = 'Dark Elf'
        self.assertEqual(char.get_ac(), 15)

        char.race = 'Grotesque'
        self.assertEqual(char.get_ac(), 16)