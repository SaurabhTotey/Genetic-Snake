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
        self.master.after(17, lambda: self.draw(game, self.master))
        self.master.mainloop()

    def draw(self, game, root):
        self.canvas.create_text(0, 0, text="HELLO WORLD")
        root.after(17, lambda: self.draw(game, root))