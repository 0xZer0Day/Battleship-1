#!/usr/bin/env python3

# Carrier (4), Battleship (3), Cruiser (2), Destroyer (1)

# format of coordinates: [[2,3],[2,4],[2,5]]

class Ship:
    def __init__(self, coordinates):
        self.is_active = True
        self.coordinates = []
        for i in range(len(coordinates)):
            self.coordinates.append(coordinates[i])

    def get_coordinates(self):
        return self.coordinates

    def get_is_active(self):
        return self.is_active

    def set_inactive(self):
        self.is_active = False


class Carrier(Ship):
    def __init__(self, coordinates):
        Ship.__init__(self, coordinates)


class Battleship(Ship):
    def __init__(self, coordinates):
        Ship.__init__(self, coordinates)


class Cruiser(Ship):
    def __init__(self, coordinates):
        Ship.__init__(self, coordinates)


class Destroyer(Ship):
    def __init__(self, coordinates):
        Ship.__init__(self, coordinates)
