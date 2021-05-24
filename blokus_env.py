import gym
import numpy as np

# 14x14 196 squares
# 21x2 42 pieces
# game state = 196 vec + ego's pieces + oppo's pieces

class BlokusEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # board obervation
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(14,14,1), dtype=np.uint8)

        # available actions: pass + 21 pieces
        self.action_space = gym.spaces.Discrete(85) # simplified 68, full 85

        # starting state
        self.state = np.zeros((14,14,1))
        self.ego_pieces = np.ones(21)
        self.op_pieces = np.ones(21)

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


def admissible_actions(state, player):
    """
    Return available actions
    legend:
    0 - pass    4 - (3)sml L    8 - (4)O        12 - (5)lg Z    16 - (5)lg T    20 - (5)ZT
    1 - (1)dot  5 - (4)4x1      9 - (4)Z        13 - (5)lg O    17 - (5)side L  21 - (5)X
    2 - (2)2x1  6 - (4)L        10 - (5)5x1     14 - (5)C       18 - (5)W
    3 - (3)3x1  7 - (4)T        11 - (5)lg L    15 - (5)side T  19 - (5)side Z
    :param state: current state
    :param player: current player
    :return: list actions: all available actions by player
    """
    open_set = np.ones(68)

    pass


#testing ground
# env = BlokusEnv()

open_set = np.zeros((14,14,1))
print(open_set.shape)