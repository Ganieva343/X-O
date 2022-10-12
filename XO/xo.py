from tkinter import *

tk = Tk()
width = 600
third = width / 3
canvas = Canvas(width=width, height=width)
tk.title = "Tic Tac Toe"

line1 = canvas.create_line(200, 0, 200, 600)
line2 = canvas.create_line(400, 0, 400, 600)
line3 = canvas.create_line(0, 200, 600, 200)
line4 = canvas.create_line(0, 400, 600, 400)

game_board = [['' for x in range(3)] for y in range(3)]

class XsorOs:
    def __init__(self):
        self.turn = 0
        self.clicked = []
    def click(self, row, col):
        if (row, col) not in self.clicked:
            if self.turn % 2 == 0:
                canvas.create_line(col * third, row * third, (col + 1) * third, (row + 1) * third)
                canvas.create_line((col + 1) * third, row * third, col * third, (row + 1) * third)
                self.turn += 1
                game_board[row][col] = 'x'

            elif self.turn % 2 == 1:
                canvas.create_oval(col * third + 5, row * third + 5, (col + 1) * third - 5, (row + 1) * third - 5)
                self.turn += 1
                game_board[row][col] = 'o'
        ## add some if statements to detect diagonals, horizontals and verticals in a row.

def mouse_click(c, event):
    col = int(event.x / third)
    row = int(event.y / third)
    c.click(row, col)


xo = XsorOs()
canvas.pack()
canvas.bind("<Button-1>", lambda event: mouse_click(xo, event))
canvas.mainloop()