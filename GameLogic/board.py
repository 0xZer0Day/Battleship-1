from .ship import Carrier, Battleship, Cruiser, Destroyer


class Board:
    def __init__(self):
        self.board = self.construct_empty_board()
        self.carrier1 = None
        self.battleship1 = None
        self.battleship2 = None
        self.cruiser1 = None
        self.cruiser2 = None
        self.cruiser3 = None
        self.destroyer1 = None
        self.destroyer2 = None
        self.destroyer3 = None
        self.destroyer4 = None
        self.ships = [self.carrier1, self.battleship1, self.battleship2,
                        self.cruiser1, self.cruiser2, self.cruiser3,
                        self.destroyer1, self.destroyer2, self.destroyer3,
                        self.destroyer4]

    def construct_empty_board(self):
        # 10 rows
        # 10 columns
        # every field contains a list with the following format:
        #   [shipname, field_is_selected]
        # if there is no ship on a field the shipname is "o"
        board = []
        row = []
        for i in range (0, 10):
            for j in range (0, 10):
                row.append(["o",0])
            board.append(row)
            row = []
        return board


class BoardAttack(Board):
    def __init__(self):
        Board.__init__(self)

    def turn_attack(self, coordinates, hit, deadly_hit):
        # Kennzeichnung des Boards für den Spieler
        # kein Rückgabewert
        self.board[coordinates[0]][coordinates[1]][1] = 1
        if hit:
            pass
        pass
        # [shipname, field_is_selected]



class BoardDefense(Board):
    def __init__(self, defense_coordinates):
        Board.__init__(self)
        self.initialize_coordinates(defense_coordinates)
        self.initialize_ships(defense_coordinates)

    def initialize_ships(self, coordinates):
        coordinates_carrier1 = []
        coordinates_battleship1 = []
        coordinates_battleship2 = []
        coordinates_cruiser1 = []
        coordinates_cruiser2 = []
        coordinates_cruiser3 = []
        coordinates_destroyer1 = []
        coordinates_destroyer2 = []
        coordinates_destroyer3 = []
        coordinates_destroyer4 = []

        for i in range(len(coordinates)):
            if coordinates[i][0] == "carrier1":
                coordinates_carrier1.append([coordinates[i][1], coordinates[i][2]])
            elif coordinates[i][0] == "battleship1":
                coordinates_battleship1.append([coordinates[i][1], coordinates[i][2]])
            elif coordinates[i][0] == "battleship2":
                coordinates_battleship2.append([coordinates[i][1], coordinates[i][2]])
            elif coordinates[i][0] == "cruiser1":
                coordinates_cruiser1.append([coordinates[i][1], coordinates[i][2]])
            elif coordinates[i][0] == "cruiser2":
                coordinates_cruiser2.append([coordinates[i][1], coordinates[i][2]])
            elif coordinates[i][0] == "cruiser3":
                coordinates_cruiser3.append([coordinates[i][1], coordinates[i][2]])
            elif coordinates[i][0] == "destroyer1":
                coordinates_destroyer1.append([coordinates[i][1], coordinates[i][2]])
            elif coordinates[i][0] == "destroyer2":
                coordinates_destroyer2.append([coordinates[i][1], coordinates[i][2]])
            elif coordinates[i][0] == "destroyer3":
                coordinates_destroyer3.append([coordinates[i][1], coordinates[i][2]])
            else:
                coordinates_destroyer4.append([coordinates[i][1], coordinates[i][2]])

        self.carrier1 = Carrier(coordinates_carrier1)
        self.battleship1 = Battleship(coordinates_battleship1)
        self.battleship2 = Battleship(coordinates_battleship2)
        self.cruiser1 = Cruiser(coordinates_cruiser1)
        self.cruiser2 = Cruiser(coordinates_cruiser2)
        self.cruiser3 = Cruiser(coordinates_cruiser3)
        self.destroyer1 = Destroyer(coordinates_destroyer1)
        self.destroyer2 = Destroyer(coordinates_destroyer2)
        self.destroyer3 = Destroyer(coordinates_destroyer3)
        self.destroyer4 = Destroyer(coordinates_destroyer4)

    def initialize_coordinates(self, coordinates):
        for i in range(0, len(coordinates)):
            self.board[coordinates[i][1]][coordinates[i][2]][0] = coordinates[i][0]

    def turn_defense(self, coordinates):
        # returns hit, deadly_hit, win

        hit = False
        deadly_hit = False
        win = False

        # Enter coordinate in board
        self.board[coordinates[0]][coordinates[1]][1] = 1

        shipname = self.board[coordinates[0]][coordinates[1]][0]

        # Check for hit
        if shipname != "o":
            hit = True

            # Check for deadly hit
            ship = self.select_ship(shipname)
            deadly_hit = True
            for ship_coordinate in ship.get_coordinates():
                if self.board[ship_coordinate[0]][ship_coordinate[1]][1] == 0:
                    deadly_hit = False
                    break

            # Set ship inactive
            if deadly_hit:
                self.set_ship_inactive(shipname)

            # Check for win
            for ship in self.ships:
                win = True
                if ship.get_is_active() == True:
                    win = False
                    break

        return [hit, deadly_hit, win]

    def select_ship(self, shipname):
        if shipname == "carrier1":
            return self.carrier1
        elif shipname == "battleship1":
            return self.battleship1
        elif shipname == "battleship2":
            return self.battleship2
        elif shipname == "cruiser1":
            return self.cruiser1
        elif shipname == "cruiser2":
            return self.cruiser2
        elif shipname == "cruiser3":
            return self.cruiser3
        elif shipname == "destroyer1":
            return self.destroyer1
        elif shipname == "destroyer2":
            return self.destroyer2
        elif shipname == "destroyer3":
            return self.destroyer3
        else:
            return self.destroyer4

    def set_ship_inactive(self, shipname):
        if shipname == "carrier1":
            self.carrier1.set_inactive()
        elif shipname == "battleship1":
            self.battleship1.set_inactive()
        elif shipname == "battleship2":
            self.battleship2.set_inactive()
        elif shipname == "cruiser1":
            self.cruiser1.set_inactive()
        elif shipname == "cruiser2":
            self.cruiser2.set_inactive()
        elif shipname == "cruiser3":
            self.cruiser3.set_inactive()
        elif shipname == "destroyer1":
            self.destroyer1.set_inactive()
        elif shipname == "destroyer2":
            self.destroyer2.set_inactive()
        elif shipname == "destroyer3":
            self.destroyer3.set_inactive()
        else:
            self.destroyer4.set_inactive()


if __name__ == "__main__":
    # defense_coordinates = [["carrier1", 2, 4], ["battleship1", 9, 9]]
    # board = BoardDefense(defense_coordinates)
    # print(board.board)
    board = BoardAttack()
    print(board.board)
