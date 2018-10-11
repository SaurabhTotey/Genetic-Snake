import math

class SnakeBlock():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isInitialized = False

    def move(self, xChange, yChange):
        self.x += xChange
        self.y += yChange
        self.isInitialized = True



class SnakeGame():

    def __init__(self):
        self.width = 20
        self.height = 35
        self.snakeX = self.width / 2
        self.snakeY = self.height / 2
        self.snake = [SnakeBlock(self.width / 2, math.floor(self.height / 2)), SnakeBlock(self.width / 2, math.floor(self.height / 2) - 1)]
        self.snakeDirection = [0, 1]
        self.queueDirection = None

    def step(self):
        if self.queueDirection != None:
            self.snakeDirection = self.queueDirection
        self.queueDirection = None
        oldX = self.snake[0].x
        oldY = self.snake[0].y
        self.snake[0].move(self.snakeDirection[0], self.snakeDirection[1])
        for i in range(1, len(self.snake)):
            newOldX = self.snake[i].x
            newOldY = self.snake[i].y
            self.snake[i].move(oldX - newOldX, oldY - newOldY)
            oldX = newOldX
            oldY = newOldY
        #If apple was consumed, extend snake

    def isValid(self):
        #Check that snake doesn't intersect with itself or walls
        pass