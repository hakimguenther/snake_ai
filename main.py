import turtle as turtle
import time as time
from agent import Agent
from snake import Snake
from game_logic import Game_logic
from food import Food
from environment import Environment

screen = turtle.Screen()
screen.setup(700, 750)

snake = Snake()
food = Food(snake)
environment = Environment(snake,food)
agent = Agent(snake, environment)
game_logic = Game_logic(snake,screen,agent,food,environment)

screen.listen()
screen.onkey(snake.moveLeft, "Left")
screen.onkey(snake.moveRight, "Right")
screen.onkey(snake.moveUp, "Up")
screen.onkey(snake.moveDown, "Down")

game_logic.startGame()
screen.exitonclick()