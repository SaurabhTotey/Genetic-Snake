import math
import SnakeGame
import SnakeLearner
import tkinter

class SnakeWindow(tkinter.Frame):

    cellSize = 50

    def __init__(self, game, learner):
        super().__init__(width=game.width * self.cellSize, height=game.height * self.cellSize)
        self.learner = learner
        if learner != None:
            self.best_moveset = learner.best_of_generation()
            self.generation = 1
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
            game.queue_direction([0, -1])
        elif event.char == "a":
            game.queue_direction([-1, 0])
        elif event.char == "s":
            game.queue_direction([0, 1])
        elif event.char == "d":
            game.queue_direction([1, 0])

    def draw(self, game, root, counter):
        if counter % (15 if self.learner == None else 1) == 0:
            if self.learner != None:
                game.queue_direction(SnakeLearner.direction_of_move(self.best_moveset.pop(0)))
                if game.step():
                    game = SnakeGame.SnakeGame()
                    self.best_moveset = self.learner.best_of_generation()
                    self.generation += 1
            else:
                if game.step():
                    return
        self.canvas.delete("all")
        self.drawBlock(game.apple_x, game.apple_y, "#f00", "#fff")
        block = game.head
        while block != None:
            self.drawBlock(block.x, block.y, "#000", "#fff")
            block = block.next_block
        self.canvas.create_text(game.width * self.cellSize - 30, 30, anchor=tkinter.NE, text=("Score: " + str(game.score)), font=("Times", 20))
        if self.learner != None:
            self.canvas.create_text(30, game.height * self.cellSize - 30, anchor=tkinter.SW, text=("Generation: " + str(self.generation)), font=("Times", 20))
        root.after(17, lambda: self.draw(game, root, counter + 1))

    def drawBlock(self, row, col, fill, stroke):
        x = row * self.cellSize
        y = col * self.cellSize
        self.canvas.create_rectangle(x, y, x + self.cellSize, y + self.cellSize, outline=stroke, fill=fill)
