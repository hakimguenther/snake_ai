import random as r
import time
from environment import Environment as env
from environment import GameState
import math
import util


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
        self.isEnd = False
        self.steps_per_episode = []
    
    def makeMove(self, direction):
        if direction == "north":
            self.snake.moveUp()
        elif direction == "east":
            self.snake.moveRight()
        elif direction == "south":
            self.snake.moveDown()
        else:
            self.snake.moveLeft()

    def getDistanceToWall(self,gameState: GameState):
        minDistance = 1

        if self.env.getState().snake_head in self.env.walls:
            minDistance = 0

        return minDistance
    
    #field is the next field for the head after an action
    #state is the next state which reward is calculated
    def getReward(self, field, state):
        food_x, food_y = state.food_position
        snake_x, snake_y = state.snake_head
        distance = util.euclideDistance((food_x,food_x),(snake_x, snake_y))
        distanceReward = 50 - distance
        if distance < 2:
            return 200
        if field == "X":
            return -100
        return distanceReward
    
    def chooseAction(self):
        max_next_reward = -1000
        best_action = ""
        next_reward = -100

        if r.random() < self.exp_rate:
            best_action = r.choice(self.env.getLegalMoves())
        else:
            current_state = self.env.getState()
            for action in self.env.getLegalMoves():
                if current_state in self.Q_values.keys():
                    if action in self.Q_values[current_state]:
                        next_reward = self.Q_values[current_state][action]
                else:
                    next_reward = 0 

                if next_reward > max_next_reward:
                    max_next_reward = next_reward
                    best_action = action

        return best_action
 
    def play(self):
        if not self.isEnd:
            action = self.chooseAction()

            current_state = self.env.getState()
            self.steps_per_episode.append([current_state, action])
            self.makeMove(action)

            field = self.env.getState().close_env[action]
            reward = self.getReward(field, self.env.getStateFromOnlyAction(action))           
            
            if reward == -100:
                self.isEnd = True

        else:
            #death is always -100 reward
            reward = -100
            current_state = self.env.getState
            for a in self.env.getLegalMoves():
                     
                if current_state in self.Q_values.keys():
                    if a in self.Q_values[current_state]:
                        self.Q_values[current_state][a] = reward
                else:
                    action_dict = {}
                    action_dict[a] = reward
                    self.Q_values[current_state] = action_dict

            ## speichern aktuelles qvalue
            ## ersetzen erst nach berechnung des vorherigen q values
            for s in reversed(self.steps_per_episode):
                if s[0] in self.Q_values.keys():
                    if s[1] in self.Q_values[s[0]]:
                        current_q_value = self.Q_values[s[0]][s[1]]
                        field =s[0].close_env[s[1]]
                        r = self.getReward(field,self.env.getStateFromAction(s[1],s[0]))
                        max_q_nxt = 0
                        for a in self.env.getLegalMoves():
                            if s[0] in self.Q_values.keys():
                                if a in self.Q_values[current_state]:
                                    if max_q_nxt > self.Q_values[current_state][a]:
                                        max_q_nxt = self.Q_values[current_state][a]
                            else:
                                action_dict = {}
                                action_dict[a] = 0
                                self.Q_values[current_state] = action_dict

                        reward = current_q_value + self.lr * (r + 0.8 * max_q_nxt - current_q_value)
                        self.Q_values[s[0]][s[1]] = round(reward, 3)
                        print("Q_Value:   ", self.Q_values[s[0]][s[1]])
                else:
                    action_dict = {}
                    action_dict[s[1]] = 0
                    self.Q_values[s[0]] = action_dict
                    print("Q_Value:   ", self.Q_values[s[0]][s[1]])

            self.steps_per_episode.clear()
            self.isEnd = False
            return -1