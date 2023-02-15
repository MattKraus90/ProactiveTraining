import datetime
import os
import numpy as np

from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import BaseCallback, EvalCallback
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.results_plotter import load_results, ts2xy

import custom_environment


class SaveOnBestTrainingRewardCallback(BaseCallback):
    """
    Callback for saving a model (the check is done every ``check_freq`` steps)
    based on the training reward (in practice, we recommend using ``EvalCallback``).

    :param check_freq: (int)
    :param log_dir: (str) Path to the folder where the model will be saved.
      It must contains the file created by the ``Monitor`` wrapper.
    :param verbose: (int)
    """

    def __init__(self, check_freq, log_dir, verbose=1):
        super(SaveOnBestTrainingRewardCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.log_dir = log_dir
        self.save_path = os.path.join(log_dir, 'best_model')
        self.best_mean_reward = -np.inf

    def _init_callback(self) -> None:
        # Create folder if needed
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self) -> bool:
        if self.n_calls % self.check_freq == 0:

            # Retrieve training reward
            x, y = ts2xy(load_results(self.log_dir), 'timesteps')
            if len(x) > 0:
                # Mean training reward over the last 100 episodes
                mean_reward = np.mean(y[-50:])
                if self.verbose > 0:
                    print("Num timesteps: {}".format(self.num_timesteps))
                    print(
                        "Best mean reward: {:.2f} - Last mean reward per episode: {:.2f}".format(self.best_mean_reward,
                                                                                                 mean_reward))

                # New best model, you could save the agent here
                if mean_reward > self.best_mean_reward:
                    self.best_mean_reward = mean_reward
                    # Example for saving best model
                    if self.verbose > 0:
                        print("Saving new best model at {} timesteps".format(x[-1]))
                        print("Saving new best model to {}.zip".format(self.save_path))
                    self.model.save(self.save_path)

        return True


eval_env = Monitor(custom_environment.CustomUserSimulatorEnvStepNumber())


# env = custom_environment.CustomUserSimulatorEnvComplexity()


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
    model = DQN('MlpPolicy', env, learning_rate=0.00005, batch_size=64, buffer_size=100000, learning_starts=0,
                target_update_interval=500, gradient_steps=1, exploration_fraction=0.15,
                exploration_final_eps=0.1, policy_kwargs=dict(net_arch=[256, 256], normalize_images=False),verbose=1)
    # model = DQN.load("trained_models/dqn_proactivity_agent", env=env)
    # Train the agent
    model.learn(total_timesteps=int(300000), callback=eval_callback)
    # Save the agent
    model.save("trained_models/dqn_proactivity_agent_optimised")



def load_test_dqn():
    # Load the trained agent
    model = DQN.load("trained_models/dqn/12_16_2021_18_45/best_model")

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
    load_test_dqn()
    t2 = datetime.datetime.now()
    print(t2 - t1)
