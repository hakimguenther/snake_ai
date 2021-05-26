import random as r
import time
from environment import Environment
import math

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

    # wallPositions = Liste der Positionen der Walls im 28 * 28 list
    # finde die nächste WallPosition aus der List
    # berechne Distanz zu nächsten wall
    # euclide 
    
    def getDistanceToWall(self, wallPosition, headPosition):
        # headPosition = 14,15
        # nächste Wall = 14, 28
        min_distance = 1000
        print(headPosition)
        for wall in wallPosition:
            wall_y, wall_x = wall
            head_y , head_x = headPosition
            distance = math.sqrt((wall_x - head_x)**2 + (wall_y - head_y)**2)
            if distance < min_distance:
                min_distance = distance
        return min_distance
        
        
        