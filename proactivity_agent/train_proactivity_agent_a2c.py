import datetime
import os
import numpy as np

from stable_baselines3 import A2C
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import BaseCallback, EvalCallback
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.env_util import make_vec_env

import custom_environment

# env = make_vec_env(lambda: env, n_envs=1)
eval_env = Monitor(custom_environment.CustomUserSimulatorEnvStepNumber())


# env = custom_environment.CustomUserSimulatorEnvComplexity()


def train_a2c():
    date_time = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M")
    model_path = 'trained_models/a2c/' + date_time + '/'
    log_path = model_path + 'logs/'
    os.makedirs(log_path + 'log/', exist_ok=True)

    env = Monitor(custom_environment.CustomUserSimulatorEnvStepNumber(), log_path + 'log/')

    # Initiate EvalCallback to save due the training the best model
    eval_callback = EvalCallback(eval_env, best_model_save_path=model_path,
                                 log_path=log_path, eval_freq=500, n_eval_episodes=12,
                                 deterministic=True, render=False)
    # Instantiate the agent
    model = A2C('MlpPolicy', env, verbose=1)
    # model = A2C.load("trained_models/a2c_proactivity_agent", env=env)
    # Train the agent
    model.learn(total_timesteps=int(20e5), callback=eval_callback)
    # Save the agent
    # model.save("trained_models/a2c_proactivity_agent")


def load_test_a2c():
    # Load the trained agent
    model = A2C.load("trained_models/a2c/12_20_2021_18_05/best_model")

    # Evaluate the agent
    # mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=12, deterministic=True)

    # Enjoy trained agent
    obs = eval_env.reset()
    print('observation: ', obs)
    cum_reward = 0
    for i in range(60):
        action, _states = model.predict(obs, deterministic=True)
        print('action: ', action)
        obs, rewards, dones, info = eval_env.step(action)
        print('observation: ', obs, '||| reward: ', rewards)
        # print('action: ', action, '||| observation: ', obs, '||| reward: ', rewards)
        cum_reward += rewards
        if dones:
            print('cum_reward: ', cum_reward)
            print('----------------------------')
            obs = eval_env.reset()
            print('observation: ', obs)
            cum_reward = 0

    # Evaluate the agent
    # for n in [10, 20, 40, 80, 120]:
    #     print(n)
    #     for j in range(5):
    #         mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=n, deterministic=True)
    #         print('mean_reward: ', mean_reward, 'std_reward: ', std_reward)
    mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=1000, deterministic=True)
    print('mean_reward: ', mean_reward, 'std_reward: ', std_reward)


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    # train_a2c()
    print('#######################')
    load_test_a2c()
    t2 = datetime.datetime.now()
    print(t2 - t1)
