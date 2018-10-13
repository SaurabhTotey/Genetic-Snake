import math
import tkinter

class SnakeWindow(tkinter.Frame):

    cellSize = 50

    def __init__(self, game):
        super().__init__(width=game.width * self.cellSize, height=game.height * self.cellSize)
        self.pack()
        self.pack_propagate(0)
        self.master.resizable(0, 0)
        self.master.title("Snake!")
        self.canvas = tkinter.Canvas(self)
        self.canvas.pack(fill=tkinter.BOTH, expand=1)
        self.master.after(17, lambda: self.draw(game, self.master, 1))
        self.master.mainloop()

    def draw(self, game, root, counter):
        if counter % 15 == 0:
            if not game.step():
                return
        self.canvas.delete("all")
        self.drawBlock(game.appleX, game.appleY, "#f00", "#fff")
        for block in game.snake:
            self.drawBlock(block.x, block.y, "#000", "#fff")
        self.canvas.create_text(game.width * self.cellSize - 30, 30, anchor=tkinter.NE, text=("Score: " + str(game.score)), font=("Times", 20))
        root.after(17, lambda: self.draw(game, root, counter + 1))

    def drawBlock(self, row, col, fill, stroke):
        x = row * self.cellSize
        y = col * self.cellSize
        self.canvas.create_rectangle(x, y, x + self.cellSize, y + self.cellSize, outline=stroke, fill=fill)
