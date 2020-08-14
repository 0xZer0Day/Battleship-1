import sys
sys.path.insert(0,'..')

from GameLogic import Game


name1 = "Lukas"
name2 = "Janos"
defense_coordinates1 = [["cruiser1", 0, 0], ["cruiser1", 0, 1],
                    ["cruiser2", 0, 3], ["cruiser2", 0, 4],
                    ["cruiser3", 0, 6], ["cruiser3", 0, 7],
                    ["carrier1", 2, 0], ["carrier1", 2, 1], ["carrier1", 2, 2], ["carrier1", 2, 3],
                    ["battleship1", 2, 5], ["battleship1", 2, 6], ["battleship1", 2, 7],
                    ["battleship2", 4, 0], ["battleship2", 4, 1], ["battleship2", 4, 2],
                    ["destroyer1", 4, 4], ["destroyer2", 4, 6], ["destroyer3", 4, 8], ["destroyer4", 6, 0]]
defense_coordinates2 = [["cruiser1", 9, 9], ["cruiser1", 9, 8],
                    ["cruiser2", 9, 6], ["cruiser2", 9, 5],
                    ["cruiser3", 9, 3], ["cruiser3", 9, 2],
                    ["carrier1", 7, 9], ["carrier1", 7, 8], ["carrier1", 7, 7], ["carrier1", 7, 6],
                    ["battleship1", 7, 4], ["battleship1", 7, 3], ["battleship1", 7, 2],
                    ["battleship2", 5, 9], ["battleship2", 5, 8], ["battleship2", 5, 7],
                    ["destroyer1", 5, 5], ["destroyer2", 5, 3], ["destroyer3", 5, 1], ["destroyer4", 3, 9]]
game = Game(name1, name2, defense_coordinates1, defense_coordinates2)

# print(game.player1.board_defense.board)
# print("\n\n")
# print(game.player1.board_attack.board)
# print("\n\n")
# print(game.player2.board_defense.board)
# print("\n\n")
# print(game.player2.board_attack.board)
# print("\n\n")


print("boards for next player (player1)")
boards = game.get_next_boards()
print("Player1")
print("Board defense:")
print(boards[0].board)
print("Board attack: ")
print(boards[1].board)
print("\n\n")

print("Making turn (9,9)")
game.turn([9,9])
print(game.player1.board_defense.board)
print("\n\n")
print(game.player1.board_attack.board)
print("\n\n")
print(game.player2.board_defense.board)
print("\n\n")
print(game.player2.board_attack.board)
print("\n\n")


print("Making turn (9,8)")
game.turn([9,8])
print(game.player1.board_defense.board)
print("\n\n")
print(game.player1.board_attack.board)
print("\n\n")
print(game.player2.board_defense.board)
print("\n\n")
print(game.player2.board_attack.board)
print("\n\n")


print("Making turn (9,7)")
game.turn([9,7])
print(game.player1.board_defense.board)
print("\n\n")
print(game.player1.board_attack.board)
print("\n\n")
print(game.player2.board_defense.board)
print("\n\n")
print(game.player2.board_attack.board)
print("\n\n")


print("Making turn (0, 0)")
game.turn([0,0])
print(game.player1.board_defense.board)
print("\n\n")
print(game.player1.board_attack.board)
print("\n\n")
print(game.player2.board_defense.board)
print("\n\n")
print(game.player2.board_attack.board)
print("\n\n")

# print("\n\n")
# boards = game.get_next_boards()
# print("Player2")
# print("Board defense:")
# print(boards[0].board)
# print("Board attack: ")
# print(boards[1].board)
# #
# #
# game.turn([0,1])
#
# print("\n\n")
# boards = game.get_next_boards()
# print("Player1")
# print("Board defense:")
# print(boards[0].board)
# print("Board attack: ")
# print(boards[1].board)
