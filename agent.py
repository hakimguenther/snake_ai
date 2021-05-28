import random as r
import time
from environment import Environment as env
from environment import GameState
import math


class Agent:

    def __init__(self,snake,enviroment: env, lr=0.1, n_steps=5, exp_rate = 0.8, episodes=15):
        self.directions = ["north","east","south","west"]
        self.snake = snake
        self.env = enviroment
        self.state_actions = []
        self.Q_values = {} 
        self.steps = n_steps
        self.exp_rate = exp_rate
        self.episodes = episodes
        self.lr = lr
        self.end = False

        
    
    def makeMove(self, direction):
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
    
    # def getDistanceToWall(self, headPosition):
    #     # wände immer bei 0 und 29 ( auf x und y)
    #     # headPosition = 14,15
    #     # nächste Wall = 14, 28
    #     min_distance = 1000

    #     if headPosition != None:
    #         head_y , head_x = headPosition
    #         if(abs(head_y - 14) > abs(head_x - 14)):
    #             if head_y > 14:
    #                 min_distance = 28 - head_y
    #             else:
    #                 min_distance = head_y
    #         else:
    #             if head_x > 14:
    #                 min_distance = 28 - head_x
    #             else:
    #                 min_distance = head_x
    #     else:
    #         headPosition = 1,1 

    #     return min_distance

    def getDistanceToWall(self,gameState: GameState):
        minDistance = 1

        if self.env.getState().snake_head in self.env.walls:
            minDistance = 0

        return minDistance
    
    #field is the next field for the head after an action
    def getReward(self, field):
        if field == "X":
            return -100
        return 1
    
    def chooseAction(self):
        max_next_reward = -1000
        best_action = ""
        if r.random() < self.exp_rate:
            best_action = r.choice(self.env.getLegalMoves())
        else:
            current_state = self.env.getState()
            for action in self.env.getLegalMoves():
                field = self.env.getState().close_env[action]
                next_reward = self.getReward(field)
                if next_reward > max_next_reward:
                    max_next_reward = next_reward
                    best_action = action
        return best_action
    
    def play(self):
        self.steps_per_episode = []

        action = self.chooseAction()
        self.state_actions.append((self.env.getState, action))

        next_state = self.env.getStateFromAction(action)
        field = self.env.getState().close_env[action]
        reward = self.getReward(field)
        #self.makeMove(action)
        current_state = self.env.getState()
        
        if current_state in self.Q_values.keys():
                if action in self.Q_values[current_state]:
                    self.Q_values[current_state][action] += 2
        else:
            action_dict = {}
            action_dict[action] = 1
            self.Q_values[current_state] = action_dict
        if reward == -100:
            self.end = True