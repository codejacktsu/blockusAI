import gym


env = gym.make('CartPole-v1')
# env.reset()
print("Observation space:", env.observation_space)
print("Shape:", env.observation_space.shape)
print("Action space:", env.action_space)
# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample()) # take a random action
# env.close()