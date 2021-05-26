import turtle 
import random as r
import time
from environment import Environment as env

class Game_logic:

    def __init__(self,snake,screen,agent,food,environment):
        self.wall_coordinates = []
        self.screen = screen
        self.snake = snake
        self.score = 0
        self.agent = agent
        self.food = food
        self.env = environment

    def wallHit(self):
        for coordinate in self.wall_coordinates:
            if self.snake.snake[0].distance(coordinate) < 15:
                return True
        return False

    def refreshScore(self):
        self.score += 1
        self.screen.getcanvas().create_rectangle(-75,-350,500,30,fill = "black")
        self.screen.getcanvas().create_text(-75,-350,fill="white",font="Times 20 italic bold",
                        text=f"Your Score: {self.score}")

    def checkFoodEaten(self):
        if self.food.food.distance(self.snake.snake[0]) < 15:
            self.refreshScore()
            self.snake.addPart()
            self.food.placeFood()
    
    def createWall_part(self,i,j):
        wall_part = turtle.Turtle("square")
        wall_part.color("white")
        wall_part.penup()
        wall_part.setpos(i,j)
        self.wall_coordinates.append(wall_part)    

    def createWall(self):
        for i in range(0,320,20):
            self.createWall_part(300,i)
            self.createWall_part(-300,i)
            self.createWall_part(300,-i)
            self.createWall_part(-300,-i)
            self.createWall_part(-i,300)
            self.createWall_part(-i,-300)
            self.createWall_part(i,300)
            self.createWall_part(i,-300)

    def startGame(self):
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.screen.tracer(0)
        self.screen.getcanvas().create_text(-75,-350,fill="white",font="Times 20 italic bold",
                        text=f"Your Score: {0}")
        self.food.placeFood()
        self.createWall()
        self.gameLoop()

    def gameLoop(self):
        while True:
            self.snake.move()
            self.checkFoodEaten()
            self.screen.update()
            time.sleep(0.05)
            print(self.agent.getDistanceToWall(self.env.walls,self.env.getSnakeHeadFromState(self.env.getCurrentState())))
   
            if self.wallHit():
                self.screen.bye()
            if self.snake.hitTail():
                self.screen.bye()
            ##self.agent.makeMove()
            ##print("Snake Tails:   ", self.env.getSnakeTailsFromState(self.env.getCurrentState()))
