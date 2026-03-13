#this will be the main game loop
from util import Util

row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
board = [row1, row2, row3]
isXTurn = True
winner = False
moves = 0
util = Util()
while not winner:
    util.print_board(board)

    choice = input("Enter your choice(1-9): ")
    
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Invalid choice! Enter a number between 1 and 9 or 'q' to quit.")

    if choice == "q":
        print("Quitting the game...")
        winner = True
    elif choice >= 1 and choice <= 9:   
        if isXTurn:
            board = util.place_symbol(choice, board, "X")
        else:
            board = util.place_symbol(choice, board, "O")

        isXTurn = not isXTurn
        moves += 1

        check_winner = util.check_winner(board, moves)
        if check_winner:
            print(check_winner)
            winner = True


util.print_board(board)