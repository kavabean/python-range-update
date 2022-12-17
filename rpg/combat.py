import random
class Combat():
    def __init__(self, 
    player_characters, 
    non_player_characters, 
    player_ply_function, 
    endgame_function):
        self.player_characters = player_characters
        self.non_player_characters = non_player_characters
        self.interactive_mode = True
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = []
        self.player_ply_function = player_ply_function
        self.endgame_function = endgame_function

    def are_characters_dead(self, characters):
        dead_characters = []
        for character in characters:
            if character.hit_point_max <= 0:
                dead_characters.append(character)
        return len(characters) == len(dead_characters)

    def is_combat_over(self):
        return self.are_characters_dead(self.player_characters) or self.are_characters_dead(self.non_player_characters)
 
    def end_combat(self):
        if not self.are_characters_dead(self.player_characters):
            self.party_success = True
        return self.party_success

    def ply(self, attacker, defender):
        hit_roll = attacker.roll_to_hit()
        hit = False
        if hit_roll > defender.get_ac():
            damage_roll = attacker.roll_for_damage()
            defender.hit_point_max = defender.hit_point_max - damage_roll
            hit = True

        return {
            "hit" : hit,
            "hit_roll" : hit_roll,
            "defender_hp" : defender.hit_point_max,
            "attacker_name" : attacker.name,
            "defender_name" : defender.name
        }
        
    def print_stats(self):
        pass
    
    def turn(self):
        for attacker in self.ordered_combatants:
            if attacker  in  self.player_characters:
                attacker_is_player = True
                defender = random.choice(self.non_player_characters) 
            else:
                attacker_is_player = False
                defender = random.choice(self.player_characters)
            result = self.ply(attacker, defender)
            self.player_ply_function(result)

            if  result["defender_hp"] <= 0:
                self.ordered_combatants.remove(defender)
                if attacker_is_player:
                    self.non_player_characters.remove(defender)
                else:
                    self.player_characters.remove(defender)
            if self.is_combat_over():
                self.end_combat()

    def start(self):
        self.ordered_combatants = self.player_characters  +   self.non_player_characters
        while not self.is_combat_over():
            winner = self.turn()

        self.endgame_function(winner)