import sys
sys.path.insert(0,'..')

from GameLogic import Game


name1 = "Hans"
name2 = "Kanns"
defense_coordinates1 = [["cruiser1", 0, 0], ["cruiser1", 0, 1]]
defense_coordinates2 = [["destroyer1", 9, 9]]
game = Game(name1, name2, defense_coordinates1, defense_coordinates2)


boards = game.get_next_boards()
print("Player1")
print("Board defense:")
print(boards[0].board)
print("Board attack: ")
print(boards[1].board)


game.turn([0,0])

print("\n\n")
boards = game.get_next_boards()
print("Player2")
print("Board defense:")
print(boards[0].board)
print("Board attack: ")
print(boards[1].board)


game.turn([0,1])

print("\n\n")
boards = game.get_next_boards()
print("Player1")
print("Board defense:")
print(boards[0].board)
print("Board attack: ")
print(boards[1].board)
