from typing import List
from snake import Snake
from food import Food

class Environment:

    def __init__(self,snake, food):
        self.snake = snake
        self.food = food
        self.walls = []
        self.getStartState()
        

    def getCurrentState(self):
        field = self.getEmptyField()
        
        # Beschaffung der food postion und umrechnen auf array wie bei schlangen position
        x,y = self.food.food.position()
        x = int(x / 20) + 14
        y = int(-y / 20) + 14
        field[y][x] = "*"

        #Beschaffung der Snake Position und einsetzen in das Field Array
        #-280 280 -> Begehbares Feld   0 0 -> Mitte des Feldes  (-40,0) (-20,0) (0,0) ->Schlange  ----> Durch 20 Teilen da Körperteilgröße 20
        # -14 bis 14 ->Begehbare Feld  0 0  -> Mitte des Feldes     ----> +14 um durch das Array zu iterieren
        # 0 bis 28 -> begehbares Feld --> 14 14 -> Mitte des Feldes
        # 1 bis 27 -> Feld im Array
        
        for i in range(len(self.snake.snake_coordinates)):
            x,y = self.snake.snake[i].position()
            x = int(x / 20) + 14
            y = int(-y / 20) + 14

            if i == 0:
                field[y][x] = "-"
            else:
                field[y][x] = "+"
            
        return field
        
    def getEmptyField(self):
        #Initiasierung des field Arrays und befüllen mit leeren Feldern(0)
        w, h = 29, 29
        field = [[str(0) for x in range(w)] for y in range(h)] 

        #Einsetzen der Wände (X)
        for i in range(0,29):
            field[i][0] = "X"
            field[i][28] = "X"
            field[0][i] = "X"
            field[28][i] = "X"

        return field

    def getStartState(self):

        field = self.getEmptyField()
        
        #Beschaffung der Snake Position und einsetzen in das Field Array
        #-280 280 -> Begehbares Feld   0 0 -> Mitte des Feldes  (-40,0) (-20,0) (0,0) ->Schlange  ----> Durch 20 Teilen da Körperteilgröße 20
        # -14 bis 14 ->Begehbare Feld  0 0  -> Mitte des Feldes     ----> +14 um durch das Array zu iterieren
        # 0 bis 28 -> begehbares Feld --> 14 14 -> Mitte des Feldes
        # 1 bis 27 -> Feld im Array
        for i in range(0, 29):
            self.walls.append((i,0))
            self.walls.append((i,28))
            self.walls.append((1,i))
            self.walls.append((27,i))
        
        for i in range(len(self.snake.snake_coordinates)):
            x,y = self.snake.snake[i].position()
            x = int(x / 20) + 14
            y = int(-y / 20) + 14
            if i == 0:
                field[y][x] = "-"
            else:
                field[y][x] = "+"

        # Beschaffung der food postion und umrechnen auf array wie bei schlangen position
        x,y = self.food.food.position()
        x = int(x / 20) + 14
        y = int(-y / 20) + 14
        field[y][x] = "*"

    # 0 - east
    # 90 - north 	
    # 180 - west	
    # 270 - south
    def getLegalMoves(self):
        directions = ["north","east","south","west"]
        
        if self.snake.snake[0].heading() == 90:
            directions.remove("south")
        if self.snake.snake[0].heading() == 180:
            directions.remove("east")
        if self.snake.snake[0].heading() == 0:
            directions.remove("west")
        if self.snake.snake[0].heading() == 270:
            directions.remove("north")
 
        return directions    

    def getStateFromAction(self,action):
        field = self.getEmptyField()
        moves = self.getLegalMoves()

        # Beschaffung der food postion und umrechnen auf array wie bei schlangen position
        x,y = self.food.food.position()
        x = int(x / 20) + 14
        y = int(-y / 20) + 14
        field[y][x] = "*"

        #Beschaffung der Snake Position und einsetzen in das Field Array
        #-280 280 -> Begehbares Feld   0 0 -> Mitte des Feldes  (-40,0) (-20,0) (0,0) ->Schlange  ----> Durch 20 Teilen da Körperteilgröße 20
        # -14 bis 14 ->Begehbare Feld  0 0  -> Mitte des Feldes     ----> +14 um durch das Array zu iterieren
        # 0 bis 28 -> begehbares Feld --> 14 14 -> Mitte des Feldes
        # 1 bis 27 -> Feld im Array
        
        for i in range(len(self.snake.snake_coordinates)):
            x,y = self.snake.snake[i].position()
            x = int(x / 20) + 14
            y = int(-y / 20) + 14
            if(action in moves):
                if action == "north":
                    y -= 1
                elif action == "south":
                    y += 1
                elif action == "east":
                    x += 1
                elif action == "west":
                    x -=1
            else:
                return None

            ##Visualisation of head as "-" and body as "+"        
            if i == 0:
                field[y][x] = "-"
            else:
                field[y][x] = "+"      
        return field  

    def getSnakeHeadFromState(self, state):
        if(state != None):
            for i, x in enumerate(state):
                if "-" in x:
                    return (i,x.index("-"))

    def getFoodFromState(self, state):
        for i, x in enumerate(state):
            if "*" in x:
                return (i, x.index("*"))
    
    def getSnakeTailsFromState(self, state):
        tails = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[j][i] == "+":
                    tails.append((j,i))
        return tails