import turtle as turtle

class Snake:

    def __init__(self):
        self.snake = []
        self.snake_coordinates = []
        for i in range(3):
            snake_part = turtle.Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.setpos(-i * 20,0)
            snake_part.speed(6)
            self.snake_coordinates.append(snake_part.position())
            self.snake.append(snake_part)

    def hitTail(self):
        for i in range(4,len(self.snake)):
            if self.snake[i].distance(self.snake[0]) < 15:
                return True
        return False

    def addPart(self):
        snake_part = turtle.Turtle("square")
        snake_part.color("white")
        snake_part.speed(6)
        snake_part.penup()
        last_x, last_y = self.snake[-1].position()
        snake_part.setpos(last_x, last_y)
        self.snake_coordinates.append(snake_part.position())
        self.snake.append(snake_part)
        

    def move(self):
        x,y = self.snake[0].position()
        self.snake[0].forward(20)
        for i in range(1,len(self.snake)):
            tx,ty = self.snake[i].position()
            self.snake[i].setpos(x,y)
            x,y = tx,ty
    
    
    # 0 - east 
    # 90 - north 	
    # 180 - west 	
    # 270 - south 	

    def moveUp(self):
        if self.snake[0].heading() !=  270:
            self.snake[0].setheading(90)

    def moveRight(self):
        if self.snake[0].heading() !=  180:
            self.snake[0].setheading(0)
    
    def moveLeft(self):
        if self.snake[0].heading() !=  0:
            self.snake[0].setheading(180)

    def moveDown(self):
        if self.snake[0].heading() !=  90:
            self.snake[0].setheading(270)