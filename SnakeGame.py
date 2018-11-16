import math
import random

class SnakeBlock:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_initialized = False

    def move(self, change_X, change_Y):
        self.x += change_X
        self.y += change_Y
        self.is_initialized = True

    def __repr__(self):
        return "SnakeBlock(" + str(self.x) + ", " + str(self.y) + ", " + "is_initialized = " + str(self.is_initialized) + ")"



class SnakeGame:

    def __init__(self):
        self.width = 20
        self.height = 35
        snake_X = math.floor(self.width / 2)
        snake_Y = math.floor(self.height / 2)
        self.snake = [SnakeBlock(snake_X, snake_Y), SnakeBlock(snake_X, snake_Y)]
        self.snake_direction = [0, -1]
        self.queue_direction = None
        self.score = 0
        self.generate_apple()

    def generate_apple(self):
        self.apple_X = random.randint(0, self.width - 1)
        self.apple_Y = random.randint(0, self.height - 1)
        if any(part.x == self.apple_X and part.y == self.apple_Y for part in self.snake):
            self.generate_apple()

    def step(self):
        if self.queue_direction != None:
            self.snake_direction = self.queue_direction
        self.queue_direction = None
        old_X = self.snake[0].x
        old_Y = self.snake[0].y
        self.snake[0].move(self.snake_direction[0], self.snake_direction[1])
        for i in range(1, len(self.snake)):
            part = self.snake[i]
            if not part.is_initialized:
                part.is_initialized = True
                break
            new_old_X = part.x
            new_old_Y = part.y
            part.move(old_X - new_old_X, old_Y - new_old_Y)
            old_X = new_old_X
            old_Y = new_old_Y
        for part in self.snake:
            if part.is_initialized and any((piece != part and piece.is_initialized and piece.x == part.x and piece.y == part.y) for piece in self.snake):
                return False
            if part.x < 0 or part.x >= self.width or part.y < 0 or part.y >= self.height:
                return False
            if part.x == self.apple_X and part.y == self.apple_Y:
                self.snake.append(SnakeBlock(self.snake[-1].x, self.snake[-1].y))
                self.generate_apple()
        self.score += len([part for part in self.snake if part.is_initialized])
        return True

    def get_state(self):
        state = []
        state.append(self.snake[0].x)
        state.append(self.snake[0].y)
        state.append(self.apple_X)
        state.append(self.apple_Y)
        for i in range(0, self.width * self.height):
            state.append(1 if any(part.x == math.floor(i / self.width) and part.y == (i % self.width) for part in self.snake) else 0)
        return state
