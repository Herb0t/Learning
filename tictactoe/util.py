class Util:

    def print_board(self, board):
        for row in board:
            print(" | ".join(row))
            if row != board[-1]:
                print("-" * 10)


    def drawGame(self):
        return "Draw! The game is a draw."

    def X_winner(self):
        return "X wins!"

    def O_winner(self):
        return "O wins!"

    def check_winner(self, board, moves):
        for row in board:
            if row.count("X") == 3:
                return self.X_winner()

            if row.count("O") == 3:
                return self.O_winner()

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == "X":
                return self.X_winner()
            if board[0][col] == board[1][col] == board[2][col] == "O":
                return self.O_winner()


        if board[0][0] == board[1][1] == board[2][2] == "X":
            return self.X_winner()
        if board[0][2] == board[1][1] == board[2][0] == "X":
            return self.X_winner()

        if board[0][0] == board[1][1] == board[2][2] == "O":
            return self.O_winner()
        if board[0][2] == board[1][1] == board[2][0] == "O":
            return self.O_winner()

        if moves == 9:
            return self.drawGame()
            
    def place_symbol(self, choice, board, symbol):
        for row_index, row in enumerate(board):
            for cell_index, cell in enumerate(row):
                if cell == str(choice):
                    board[row_index][cell_index] = symbol
                    return board