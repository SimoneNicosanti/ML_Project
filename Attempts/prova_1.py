import gymnasium as gym

from stable_baselines3 import DQN

def trainModel(trainSeed : int, totalTimeSteps : int) :
    env = gym.make("MountainCar-v0")
    env.action_space.seed(trainSeed)
    env.reset(seed = trainSeed)
    
    print("HELLO")
    model = DQN("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps = totalTimeSteps, log_interval=10)
    model.save("dqn_cartpole")
    #model = DQN.load("dqn_cartpole")
    