#!/usr/bin/env python3

from .board import BoardDefense, BoardAttack


class Player:
    def __init__(self, name, defense_coordinates):
        # name: String
        # defense_coordinates: [["carrier1", 2, 4], ["battleship1", 9, 9], ...]
        #            -> [shipname: String, row: Int, column: Int]
        self.name = name
        self.board_attack = BoardAttack()
        self.board_defense = BoardDefense(defense_coordinates)

    def get_board_defense(self):
        return self.board_defense

    def get_board_attack(self):
        return self.board_attack

    def turn_attack(self, coordinates, hit, deadly_hit, dead_ship_coordinates):
        # coordinates: [3,6]
        #        -> [row, column]
        # hit: Bool
        # deadly_hit: Bool
        # dead_ship_coordinates: List
        self.board_attack.turn_attack(coordinates, hit, deadly_hit, dead_ship_coordinates)

    def turn_defense(self, coordinates):
        # coordinates: [3,6]
        #        -> [row, column]
        # returns list: [hit: Bool, deadly_hit: Bool, win: Bool, dead_ship_coordinates: List]
        return self.board_defense.turn_defense(coordinates)
