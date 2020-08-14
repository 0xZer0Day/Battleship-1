#!/usr/bin/env python3

# 1 x Carrier (4 Fields),
# 2 x Battleship (3 Fields),
# 3 x Cruiser (2 Fields),
# 4 x Destroyer (1 Field)

class Ship:
    def __init__(self, coordinates):
        # coordinates: List
        #         -> format of coordinates: [[2,3],[2,4],[2,5]]
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
        # coordinates: List
        #         -> format of coordinates: [[2,3],[2,4],[2,5]]
        Ship.__init__(self, coordinates)


class Battleship(Ship):
    def __init__(self, coordinates):
        # coordinates: List
        #         -> format of coordinates: [[2,3],[2,4],[2,5]]
        Ship.__init__(self, coordinates)


class Cruiser(Ship):
    def __init__(self, coordinates):
        # coordinates: List
        #         -> format of coordinates: [[2,3],[2,4],[2,5]]
        Ship.__init__(self, coordinates)


class Destroyer(Ship):
    def __init__(self, coordinates):
        # coordinates: List
        #         -> format of coordinates: [[2,3],[2,4],[2,5]]
        Ship.__init__(self, coordinates)
