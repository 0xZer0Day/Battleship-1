from .board import Board, BoardDefense, BoardAttack

class Player:
    def __init__(self, name, defense_coordinates):
        self.name = name
        self.board_attack = BoardAttack()
        self.board_defense = BoardDefense(defense_coordinates)

    def get_board_defense(self):
        return self.board_defense

    def get_board_attack(self):
        return self.board_attack

    def turn_attack(self, coordinates, hit, deadly_hit):
        self.board_attack.turn_attack(coordinates, hit, deadly_hit)

    def turn_defense(self, coordinates):
        message = self.board_defense.turn_defense(coordinates)
        return message