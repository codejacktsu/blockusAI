import gym
import numpy as np
from board import Board

# 14x14 196 squares
# 21x2 42 pieces
# game state = 196 vec + ego's pieces + oppo's pieces

class BlokusEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # board obervation
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(14,14,1), dtype=np.uint8)

        # available actions: 13729 possible moves
        self.action_space = gym.spaces.Discrete(13729)

        # starting state
        self.state = Board(14)


    def step(self, action):
        pass
        # return observation, reward, done, info

    def reset(self):
        pass
        # return observation  # reward, done, info can't be included

    def render(self, mode='human'):
        pass

    def close(self):
        pass



#testing ground
env = BlokusEnv()

print(env.action_space)
