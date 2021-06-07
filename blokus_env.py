import gym
import numpy as np
from board import Board, Agent
from game_pieces import EGO_PIECES, VIL_PIECES


# 14x14 196 squares
# 21x2 42 pieces
# game state = 196 vec

class BlokusEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # board obervation
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(14,14,1), dtype=np.uint8)

        # available actions: 13729 possible moves
        self.action_space = gym.spaces.Discrete(13729)

        # starting state
        self.state = Board(14)

        # init agents
        self.p1 = Agent(EGO_PIECES, 0)
        self.p2 = Agent(VIL_PIECES, 1)

        # random whon starts
        self.starting_player_idx = np.random.randint(0, 1)

    def step(self, agent):
        agent.move(self.state)
        observation = self.state.board
        reward = agent.gen_reward()
        done = self.state.done[agent.player_idx]
        info = {}
        return observation, reward, done, info

    def reset(self):
        self.state.reset()
        self.p1.reset()
        self.p2.reset()
        self.starting_player_idx = np.random.randint(0, 1)

        observation = self.state.board
        return observation

    def render(self, mode='human'):
        pass

    def close(self):
        pass



#testing ground
env = BlokusEnv()

print(env.action_space)
