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
            self.walls.append((2,i))
        
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
    
    def getState(self):
        
        snake_head_position = self.snake.snake[0].position()
        snake_body_coordinates = []
        for i in range(1,len(self.snake.snake)):
            body_x, body_y = self.snake.snake[i].position()
            body_y = round(body_y / 20 + 14)
            body_x = round(body_x / 20 + 14)
            body_position = body_x, body_y
            snake_body_coordinates.append(body_position)
        
        food_position = self.food.food.position()

        food_x, food_y = food_position
        food_y = round(food_y / 20 + 14)
        food_x = round(food_x / 20 + 14)
        food_position = food_x, food_y
        
        
        snake_x, snake_y = snake_head_position
        snake_y = round(snake_y / 20 + 14)
        snake_x = round(snake_x / 20 + 14)
        snake_head_position = snake_x, snake_y
        
        
        left = snake_x - 1, snake_y
        up = snake_x, snake_y +1
        right = snake_x + 1, snake_y
        down = snake_x, snake_y -1
        directions = [left,up,right,down]
        close_env = {}
        
        for i in range(len(directions)):
            if directions[i] in self.walls:
                elem = "x"
            elif directions[i] in snake_body_coordinates:
                elem = "+"
            elif directions[i] == food_position:
                elem = "*"
            else:
                elem = "0"
            
            if i == 0:
                close_env["west"] = elem
            elif i == 1:
                close_env["north"] = elem
            elif i == 2:
                close_env["east"] = elem
            else:
                close_env["south"] = elem

        return GameState(snake_head_position, food_position,close_env)

    def getStateFromAction(self, action):
        current_state = self.getState()
        
        if action == "north":
            current_state.snake_head[0] += 1
        elif action == "south":
            current_state.snake_head[0] -= 1
        elif action == "west":
            current_state.snake_head[1] -= 1
        elif action == "east":
            current_state.snake_head[1] += 1
        
        x,y = current_state.snake_head

        #MUSS NOCH UMGERECHNET WERDEN
        for i in range(1,len(self.snake.snake)):
            tx,ty = self.snake[i].position()
            self.snake[i].setpos(x,y)
            x,y = tx,ty
        
        #Return current_state mit aktualisierten Schlangenkoordinaten

class GameState:
    def __init__(self, snake_head, food_position, close_env):
        self.snake_head = snake_head
        self.food_position = food_position
        self.close_env = close_env
    
    def __str__(self) -> str:
        return "head   ",self.snake_head, "food", self.food_position, "close_env", self.close_env