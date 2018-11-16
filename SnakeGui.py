import math
import tkinter

class SnakeWindow(tkinter.Frame):

    cellSize = 50

    def __init__(self, game, learner):
        super().__init__(width=game.width * self.cellSize, height=game.height * self.cellSize)
        self.learner = learner
        self.pack()
        self.pack_propagate(0)
        self.master.resizable(0, 0)
        self.master.title("Snake!")
        self.canvas = tkinter.Canvas(self)
        self.canvas.pack(fill=tkinter.BOTH, expand=1)
        self.focus_set()
        self.bind("<KeyPress>", lambda event: self.onKeyPress(game, event))
        self.master.after(17, lambda: self.draw(game, self.master, 1))
        self.master.mainloop()

    def onKeyPress(self, game, event):
        if self.learner != None:
            return
        if event.char == "w":
            game.queue_direction = [0, -1]
        elif event.char == "a":
            game.queue_direction = [-1, 0]
        elif event.char == "s":
            game.queue_direction = [0, 1]
        elif event.char == "d":
            game.queue_direction = [1, 0]
        if game.queue_direction[0] == -game.snake_direction[0] or game.queue_direction[1] == -game.snake_direction[1]:
            game.queue_direction = None

    def draw(self, game, root, counter):
        if counter % 15 == 0:
            if self.learner != None:
                is_alive = False #TODO get learner prediction
                if not is_alive:
                    return
            else:
                if not game.step():
                    return
        self.canvas.delete("all")
        self.drawBlock(game.apple_X, game.apple_Y, "#f00", "#fff")
        for block in game.snake:
            self.drawBlock(block.x, block.y, "#000", "#fff")
        self.canvas.create_text(game.width * self.cellSize - 30, 30, anchor=tkinter.NE, text=("Score: " + str(game.score)), font=("Times", 20))
        root.after(17, lambda: self.draw(game, root, counter + 1))

    def drawBlock(self, row, col, fill, stroke):
        x = row * self.cellSize
        y = col * self.cellSize
        self.canvas.create_rectangle(x, y, x + self.cellSize, y + self.cellSize, outline=stroke, fill=fill)
