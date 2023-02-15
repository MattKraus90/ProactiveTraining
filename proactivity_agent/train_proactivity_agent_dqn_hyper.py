import datetime
import os
import numpy as np

from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import BaseCallback, EvalCallback
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.results_plotter import load_results, ts2xy

import custom_environment

eval_env = Monitor(custom_environment.CustomUserSimulatorEnvStepNumber())


def train_dqn():
    date_time = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M")
    model_path = 'trained_models/dqn/' + date_time + '/'
    log_path = model_path + 'logs/'
    os.makedirs(log_path + 'log/', exist_ok=True)

    env = Monitor(custom_environment.CustomUserSimulatorEnvStepNumber(), log_path + 'log/')

    # Initiate EvalCallback to save due the training the best model
    eval_callback = EvalCallback(eval_env, best_model_save_path=model_path,
                                 log_path=log_path, eval_freq=500, n_eval_episodes=50,
                                 deterministic=True, render=False)
    # Instantiate the agent
    model = DQN('MlpPolicy', env, learning_rate=0.00001, batch_size=16, buffer_size=100000, learning_starts=0,
                target_update_interval=500, gradient_steps=1, exploration_fraction=0.12,
                exploration_final_eps=0.1, policy_kwargs=dict(net_arch=[32, 32]), verbose=1)
    # model = DQN.load("trained_models/dqn_proactivity_agent", env=env)
    # Train the agent
    model.learn(total_timesteps=int(20000), callback=eval_callback)
    # Save the agent
    # model.save("trained_models/dqn_proactivity_agent")


def load_test_dqn():
    # Load the trained agent
    model = DQN.load("trained_models/dqn/12_15_2021_23_11/best_model")

    # Evaluate the agent
    # mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=20)

    # Enjoy trained agent
    obs = eval_env.reset()
    cum_reward = 0
    for i in range(60):
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, dones, info = eval_env.step(action)
        print('action: ', action, '||| observation: ', obs)
        cum_reward += rewards
        if dones:
            print('cum_reward: ', cum_reward)
            print('----------------------------')
            obs = eval_env.reset()
            cum_reward = 0

    for n in [10, 20, 40, 80, 120]:
        print(n)
        for j in range(5):
            mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=n, deterministic=True)
            print('mean_reward: ', mean_reward, 'std_reward: ', std_reward)


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    train_dqn()
    print('#######################')
    # load_test_dqn()
    t2 = datetime.datetime.now()
    print(t2 - t1)
