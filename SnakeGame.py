import math

class SnakeBlock:

    def __init__(self, x, y):
        self.is_alive = False
        self.next_block = None
        self.x = x
        self.y = y

    def move_to(self, x, y):
        if self.next_block != None:
            if self.next_block.is_alive:
                self.next_block.move_to(self.x, self.y)
            else:
                self.next_block.is_alive = True
        self.x = x
        self.y = y
    
    def grow(self):
        if self.next_block == None:
            self.next_block = SnakeBlock(self.x, self.y)
        else:
            self.next_block.grow()

    def get_size(self):
        if self.next_block == None:
            return 1
        else:
            return 1 + self.next_block.get_size()

class SnakeGame:

    def __init__(self):
        self.width = 20
        self.height = 20
        self.queued_direction = [0, -1]
        self.head = SnakeBlock(self.width / 2, int(math.floor(self.height / 2.0)))
        self.head.next_block = SnakeBlock(self.width / 2, self.head.y + 1)
        self.head.next_block.is_alive = True
        self.apple_locations = []
        self.generate_apple()
        self.score = 0

    def queue_direction(self, direction):
        if int(math.fabs(direction[0] + direction[1])) == 1:
            self.queued_direction = direction

    def generate_apple(self):
        corners = [[-1, -1], [-1, self.height], [self.width, -1], [self.width, self.height]]
        furthest_corner_distance = -1
        furthest_corner = None
        for corner in corners:
            distance = distance_between(self.head.x, self.head.y, corner[0], corner[1])
            distance += sum(distance_between(apple_location[0], apple_location[1], corner[0], corner[1]) for apple_location in self.apple_locations)
            if distance > furthest_corner_distance:
                furthest_corner_distance = distance
                furthest_corner = corner
        tail = self.head
        while tail.next_block != None:
            tail = tail.next_block
        self.apple_x = int((self.head.x + tail.x + furthest_corner[0]) / 3)
        self.apple_y = int((self.head.y + tail.y + furthest_corner[1]) / 3)
        self.apple_locations.append([self.apple_x, self.apple_y])
        current_block = self.head
        while current_block != None:
            if current_block.x == self.apple_x and current_block.y == self.apple_y:
                self.generate_apple()
                break
            current_block = current_block.next_block

    def step(self):
        snake_direction = [self.head.x - self.head.next_block.x, self.head.y - self.head.next_block.y]
        if (snake_direction[0] != 0 and snake_direction[0] == -self.queued_direction[0]) or (snake_direction[1] != 0 and snake_direction[1] == -self.queued_direction[1]):
            return True
        self.head.move_to(self.head.x + self.queued_direction[0], self.head.y + self.queued_direction[1])
        current_block = self.head.next_block
        while current_block != None:
            if current_block.x == self.head.x and current_block.y == self.head.y:
                return True
            current_block = current_block.next_block
        if self.head.x < 0 or self.head.x >= self.width or self.head.y < 0 or self.head.y >= self.height:
            return True
        if self.head.x == self.apple_x and self.head.y == self.apple_y:
            self.head.grow()
            self.generate_apple()
        self.score += self.head.get_size()
        return False

def distance_between(x1, y1, x2, y2):
    return int(math.fabs(x2 - x1) + math.fabs(y2 - y1))
