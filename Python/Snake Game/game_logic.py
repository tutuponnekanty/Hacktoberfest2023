import random

class Snake:
    def __init__(self, width, height):
        self.body = [[width//2, height//2]]
        self.direction = [0, 0]

    def move(self):
        head = self.body[-1]
        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]
        self.body.append(new_head)
        self.body.pop(0)

    def grow(self):
        tail = self.body[0]
        new_tail = [tail[0] - self.direction[0], tail[1] - self.direction[1]]
        self.body.insert(0, new_tail)

class Apple:
    def __init__(self, width, height):
        self.position = [random.randrange(1, (width//20)) * 20, random.randrange(1, (height//20)) * 20]
        self.is_food_on_screen = True

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = [random.randrange(1, (width//20)) * 20, random.randrange(1, (height//20)) * 20]
            self.is_food_on_screen = True
        return self.position

    def set_food_on_screen(self, choice):
        self.is_food_on_screen = choice
