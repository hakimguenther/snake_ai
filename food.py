import turtle as turtle
import random as r
from snake import Snake

class Food:

    def __init__(self,snake):
        food_coordinate = self.generateFoodCoordinate()
        food = turtle.Turtle("square")
        food.penup()
        food.color("yellow")
        food.setpos(food_coordinate)
        self.food = food
        self.snake = snake

    def placeFood(self):
        food_coordinate = self.generateFoodCoordinate()

        while(food_coordinate in self.snake.snake_coordinates):
            food_coordinate = self.generateFoodCoordinate()
        self.food.setpos(food_coordinate)        


    def generateFoodCoordinate(self):
        x = r.randrange(-280, 280, 20)
        y = r.randrange(-280, 280, 20)
        return (x,y)
