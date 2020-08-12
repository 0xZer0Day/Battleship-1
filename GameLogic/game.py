#!/usr/bin/env python3

from .player import Player


class Game:
    def __init__(self, name1, name2, defense_coordinates1, defense_coordinates2):
        # name1: String
        # name2: String
        # defense_coordinates1, defense_coordinates2 = [["carrier1", 2, 4], ["battleship1", 9, 9], ...]
        #   -> [shipname, row, column]
        self.player1 = Player(name1, defense_coordinates1)
        self.player2 = Player(name2, defense_coordinates2)
        self.current_player = 1

    def get_next_boards(self):
        # returns a list consisting of current player's defense board and other
        # player's attack board
        board_defense = None
        board_attack = None
        if self.current_player == 1:
            board_defense = self.player1.get_board_defense()
            board_attack = self.player2.get_board_attack()
        else:
            board_defense = self.player2.get_board_defense()
            board_attack = self.player1.get_board_attack()
        return [board_defense, board_attack]

    def turn(self, coordinates):
        # coordinates: [3,6]
        #   -> [row, column]
        # return message: [bool hit, bool deadly_hit, bool win]
        message = None

        while True:
            if self.current_player == 1:
                message = self.player2.turn_defense(coordinates)
                self.player1.turn_attack(coordinates, message[0], message[1])
            else:
                message = self.player1.turn_defense(coordinates)
                self.player2.turn_attack(coordinates, message[0], message[1])
            if message[0] == 0 or message[2] == 1:
                break

        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

        return message
