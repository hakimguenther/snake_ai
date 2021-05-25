import random as r
import time

class Agent:

    def __init__(self,snake):
        self.directions = ["north","east","south","west"]
        self.snake = snake
    
    def makeMove(self):
        direction = r.choice(self.directions)
        if direction == "north":
            self.snake.moveUp()
        elif direction == "east":
            self.snake.moveRight()
        elif direction == "south":
            self.snake.moveDown()
        else:
            self.snake.moveLeft()