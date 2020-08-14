#!/usr/bin/env python3

from .player import Player


class Game:
    def __init__(self, name1, name2, defense_coordinates1, defense_coordinates2):
        # name1: String
        # name2: String
        # defense_coordinates1, defense_coordinates2: [["carrier1", 2, 4], ["battleship1", 9, 9], ...]
        #            -> [shipname: String, row: Int, column: Int]
        self.player1 = Player(name1, defense_coordinates1)
        self.player2 = Player(name2, defense_coordinates2)
        self.current_player = 1

    def get_next_boards(self):
        # returns a list consisting of current player's defense and attack board
        if self.current_player == 1:
            return [self.player1.get_board_defense(), self.player1.get_board_attack()]
        return [self.player2.get_board_defense(), self.player2.get_board_attack()]

    def turn(self, coordinates):
        # coordinates: [3,6]
        #        -> [row, column]
        # return message: [hit: Bool, deadly_hit: Bool, win: Bool, dead_ship_coordinates: List]
        message = None

        if self.current_player == 1:
            message = self.player2.turn_defense(coordinates)
            self.player1.turn_attack(coordinates, message[0], message[1], message[3])
        else:
            message = self.player1.turn_defense(coordinates)
            self.player2.turn_attack(coordinates, message[0], message[1], message[3])

        # only changing current_player if there is no hit
        if message[0] == 0:
            if self.current_player == 1:
                self.current_player = 2
            else:
                self.current_player = 1

        return message
