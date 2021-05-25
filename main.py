import turtle as turtle
import time as time
from snake import Snake
from game_logic import Game_logic

screen = turtle.Screen()
screen.setup(700, 750)

snake = Snake()
game_logic = Game_logic(snake,screen)

screen.listen()
screen.onkey(snake.moveLeft, "Left")
screen.onkey(snake.moveRight, "Right")
screen.onkey(snake.moveUp, "Up")
screen.onkey(snake.moveDown, "Down")

game_logic.startGame()

screen.exitonclick()