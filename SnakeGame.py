import math
import random

class SnakeBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isInitialized = False

    def move(self, xChange, yChange):
        self.x += xChange
        self.y += yChange
        self.isInitialized = True

    def __repr__(self):
        return "SnakeBlock(" + str(self.x) + ", " + str(self.y) + ", " + "isInitialized = " + str(self.isInitialized) + ")"



class SnakeGame:

    def __init__(self):
        self.width = 20
        self.height = 35
        snakeX = math.floor(self.width / 2)
        snakeY = math.floor(self.height / 2)
        self.snake = [SnakeBlock(snakeX, snakeY), SnakeBlock(snakeX, snakeY)]
        self.snakeDirection = [0, -1]
        self.queueDirection = None
        self.score = 0
        self.generateApple()

    def generateApple(self):
        self.appleX = random.randint(0, self.width - 1)
        self.appleY = random.randint(0, self.height - 1)
        for part in self.snake:
            if part.x == self.appleX and part.y == self.appleY:
                self.generateApple()
                break

    def step(self):
        if self.queueDirection != None:
            self.snakeDirection = self.queueDirection
        self.queueDirection = None
        oldX = self.snake[0].x
        oldY = self.snake[0].y
        self.snake[0].move(self.snakeDirection[0], self.snakeDirection[1])
        for i in range(1, len(self.snake)):
            part = self.snake[i]
            if not part.isInitialized:
                part.isInitialized = True
                break
            newOldX = part.x
            newOldY = part.y
            part.move(oldX - newOldX, oldY - newOldY)
            oldX = newOldX
            oldY = newOldY
        for part in self.snake:
            if part.isInitialized and any((piece != part and piece.isInitialized and piece.x == part.x and piece.y == part.y) for piece in self.snake):
                return False
            if part.x < 0 or part.x >= self.width or part.y < 0 or part.y >= self.height:
                return False
            if part.x == self.appleX and part.y == self.appleY:
                self.snake.append(SnakeBlock(self.snake[-1].x, self.snake[-1].y))
                self.generateApple()
        self.score += len([part for part in self.snake if part.isInitialized])
        return True
