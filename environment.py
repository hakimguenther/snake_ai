from snake import Snake
from food import Food

class Environment:

    def __init__(self,snake, food):
        self.snake = snake
        self.food = food
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
            print(f"x: {x}")
            print(f"y: {y}")
            if i == 0:
                field[y][x] = "-"
            else:
                field[y][x] = "+"
            
        
        for row in field:
            print(row)
        
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

            for move in moves:
                if move == "north":
                    y -= 1
                    print("We move north")
                elif move == "south":
                    y += 1
                    print("We move north")
                elif move == "east":
                    x += 1
                else:
                    x -=1
            print(f"x: {x}")
            print(f"y: {y}")
            if i == 0:
                field[y][x] = "-"
            else:
                field[y][x] = "+"
            
        
        for row in field:
            print(row)

    # 0 - east 
    # 90 - north 	
    # 180 - west 	
    # 270 - south 	
    def getLegalMoves(self):
        directions = ["north","east","south","west"]
        
        if self.snake.snake.heading() == 90:
            directions.remove("south")
        if self.snake.snake.heading() == 180:
            directions.remove("east")
        if self.snake.snake.heading() == 0:
            directions.remove("west")
        if self.snake.snake.heading() == 270:
            directions.remove("north")
 
        return directions

    def getStartState(self):
        field = self.getEmptyField()
        
        #Beschaffung der Snake Position und einsetzen in das Field Array
        #-280 280 -> Begehbares Feld   0 0 -> Mitte des Feldes  (-40,0) (-20,0) (0,0) ->Schlange  ----> Durch 20 Teilen da Körperteilgröße 20
        # -14 bis 14 ->Begehbare Feld  0 0  -> Mitte des Feldes     ----> +14 um durch das Array zu iterieren
        # 0 bis 28 -> begehbares Feld --> 14 14 -> Mitte des Feldes
        # 1 bis 27 -> Feld im Array

        for i in range(len(self.snake.snake_coordinates)):
            x,y = self.snake.snake[i].position()
            x = int(x / 20) + 14
            y = int(-y / 20) + 14
            print(f"x: {x}")
            print(f"y: {y}")
            if i == 0:
                field[y][x] = "-"
            else:
                field[y][x] = "+"

        # Beschaffung der food postion und umrechnen auf array wie bei schlangen position
        x,y = self.food.food.position()
        x = int(x / 20) + 14
        y = int(-y / 20) + 14
        field[y][x] = "*"

        field[::-1]
        for row in field:
            print(row)