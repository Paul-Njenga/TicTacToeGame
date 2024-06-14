import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click)
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack()
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.single_player = False
        self.game_over = False
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100)
            self.canvas.create_line(i * 100, 0, i * 100, 300)
        
        for r in range(3):
            for c in range(3):
                if self.board[r][c] != " ":
                    x = c * 100 + 50
                    y = r * 100 + 50
                    self.canvas.create_text(x, y, text=self.board[r][c], font=("Arial", 48))

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def check_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def click(self, event):
        if self.game_over:
            return
        row, col = event.y // 100, event.x // 100
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.draw_board()
            winner = self.check_winner()
            if winner:
                self.canvas.create_text(150, 150, text=f"{winner} wins!", font=("Arial", 24))
                self.game_over = True
            elif self.check_draw():
                self.canvas.create_text(150, 150, text="Draw!", font=("Arial", 24))
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.single_player and self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
        row, col = random.choice(empty_cells)
        self.board[row][col] = "O"
        self.draw_board()
        winner = self.check_winner()
        if winner:
            self.canvas.create_text(150, 150, text=f"{winner} wins!", font=("Arial", 24))
            self.game_over = True
        elif self.check_draw():
            self.canvas.create_text(150, 150, text="Draw!", font=("Arial", 24))
            self.game_over = True
        else:
            self.current_player = "X"

    def reset(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.draw_board()

    def start_game(self, single_player=False):
        self.single_player = single_player
        self.reset()

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    
    menu = tk.Menu(root)
    root.config(menu=menu)
    
    mode_menu = tk.Menu(menu)
    menu.add_cascade(label="Mode", menu=mode_menu)
    mode_menu.add_command(label="Single Player", command=lambda: game.start_game(single_player=True))
    mode_menu.add_command(label="Multiplayer", command=lambda: game.start_game(single_player=False))
    
    root.mainloop()

if __name__ == "__main__":
    main()
    