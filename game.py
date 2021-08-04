import tkinter as tk


class Board(object):
    turn = 0
    texts = ("X", "O")
    colors = ("gray", "white")

    @classmethod
    def next_turn(cls):
        cls.turn += 1

    def __init__(self, master, board_size):
        self.master = master
        self.board_size = board_size
        self.canvas = tk.Canvas(master, width=board_size, height=board_size, bg="black")
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.pack()

    @property
    def square_len(self):
        return self.board_size // 3

    @property
    def midpoint(self):
        return self.square_len // 2

    def draw_board(self):
        """creates board"""

        for row in range(3):
            for col in range(3):
                left_x = col * self.square_len  # upper left X
                upper_y = row * self.square_len  # upper left Y
                right_x = left_x + self.square_len  # lower right X
                lower_y = upper_y + self.square_len  # lower right Y

                coords = (left_x, upper_y, right_x, lower_y)
                color = self.colors[(row + col) % 2]
                self.canvas.create_rectangle(*coords, fill=color)

    def left_click(self, event):
        row, col = self.eval_square(event.x, event.y)
        print(f"row: {row}, col: {col}")

        self.next_turn()
        text = self.texts[self.turn % 2]
        self.draw_text(row, col, text)

    def eval_square(self, c_x, c_y):
        row = c_x // self.square_len
        col = c_y // self.square_len

        return row, col

    def draw_text(self, col, row, text):
        text_x = (col * self.square_len) + self.midpoint
        text_y = (row * self.square_len) + self.midpoint
        self.canvas.create_text(text_x, text_y, text=text, font=("", self.midpoint))


""" Still Require
Win condition
reset board
list of moves
"""


def main():
    root = tk.Tk()
    board_size = 600
    board = Board(root, board_size)
    board.draw_board()
    root.mainloop()


if __name__ == "__main__":
    main()
