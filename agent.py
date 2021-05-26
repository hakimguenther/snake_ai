import random as r
import time
from environment import Environment as env
import math

class Agent:

    def __init__(self,snake,enviroment, lr=0.1, n_steps=5, exp_rate = 0.8, episodes=1):
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

        # self.model = {}
        # for row in range(28):
        #     for col in range(28):
        #         self.Q_values[(row, col)] = {}
        #         for a in self.actions:
        #             self.Q_values[(row, col)][a] = 0
        
    
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
    
    def getDistanceToWall(self, headPosition):
        # wände immer bei 0 und 29 ( auf x und y)
        # headPosition = 14,15
        # nächste Wall = 14, 28
        min_distance = 1000

        if headPosition != None:
            head_y , head_x = headPosition
            if(abs(head_y - 14) > abs(head_x - 14)):
                if head_y > 14:
                    min_distance = 28 - head_y
                else:
                    min_distance = head_y
            else:
                if head_x > 14:
                    min_distance = 28 - head_x
                else:
                    min_distance = head_x
        else:
            headPosition = 1,1 

        return min_distance
    
    ##state 1 = current state
    ##state 2 = next state with action
    ##action = action
    def getReward(self,state1, state2, action):
        distance_to_wall = self.getDistanceToWall(self.env.getSnakeHeadFromState(state2))
        if distance_to_wall == 0:
            return -100        
        return 1
    
    def chooseAction(self):
        max_next_reward = -1000
        best_action = ""
        if r.random() < self.exp_rate:
            action = r.choice(self.env.getLegalMoves())
        else:
            current_state = self.env.getCurrentState()
            for action in self.env.getLegalMoves():
                next_state = self.env.getStateFromAction(action)
                next_reward = self.getReward(current_state,next_state, action)
                if next_reward > max_next_reward:
                    max_next_reward = next_reward
                    best_action = action
                    
        return best_action
    
    def play(self):
        self.steps_per_episode = []

        for ep in range(self.episodes):
                action = self.chooseAction()
                current_state = self.env.getCurrentState()
                self.state_actions.append((current_state, action))

                next_state = self.env.getStateFromAction(action)
                reward = self.getReward(current_state, next_state, action)
                print(reward)
                self.makeMove(action)
                # self.Q_values[current_state][action] += self.lr * (reward + max(self.Q_values[next_state].values()) - self.Q_values[current_state][action])
                
                if reward == -100:
                    self.end = True
                