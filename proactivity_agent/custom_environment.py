import gym
from gym import spaces
import numpy as np
from stable_baselines3.common.env_checker import check_env

# import os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# from user_simulator import us_dummy
from user_simulator.step_number_dependent import user_simulator_step
from user_simulator.complexity_dependent import user_simulator_com


class CustomUserSimulatorEnvStepNumber(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['console']}

    NONE = 0
    NOTIFICATION = 1
    SUGGESTION = 2
    INTERVENTION = 3

    def __init__(self):
        super(CustomUserSimulatorEnvStepNumber, self).__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=np.array([0, 0, 0, 0, 0]),
                                            high=np.array([1, 1, 1, 1, 1]),
                                            dtype=np.float32)  # step_number, complexity,trust, points, duration
        # self.user_simulator = us_dummy.DummyClass()
        self.user_simulator = user_simulator_step.UserSimulator()
        self.user_simulator.generate_person_data()

        self.step_number = 1

        self.points = 0
        self.reward_table_trust = {1: -1, 2: -0.5, 3: 0, 4: 0.5, 5: 1}
        self.reward_table_points = {'min': 0, '<mean': 0.25, 'mean': 0.5, '>mean': 0.75, 'max': 0.75}
        self.reward_table_duration = {'<mean': 0.25, 'mean': 0.25, '>mean': 0}
        self.max_points = [10, 10, 10, 10, 10, 30, 30, 20, 40, 20, 10, 20]
        self.complexity_list = [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3]
        self.mean_table = {1: {'points_mean': 10.0, 'duration_mean': 51.46103896103896},
                           2: {'points_mean': 8.051948051948052, 'duration_mean': 40.607142857142854},
                           3: {'points_mean': 8.116883116883116, 'duration_mean': 43.61038961038961},
                           4: {'points_mean': 6.266233766233766, 'duration_mean': 41.07142857142857},
                           5: {'points_mean': 8.116883116883116, 'duration_mean': 43.34415584415584},
                           6: {'points_mean': 20.714285714285715, 'duration_mean': 56.89935064935065},
                           7: {'points_mean': 17.727272727272727, 'duration_mean': 38.59415584415584},
                           8: {'points_mean': 14.123376623376624, 'duration_mean': 35.95454545454545},
                           9: {'points_mean': 30.0974025974026, 'duration_mean': 34.62987012987013},
                           10: {'points_mean': 9.123376623376624, 'duration_mean': 36.39935064935065},
                           11: {'points_mean': 7.435064935064935, 'duration_mean': 33.47402597402598},
                           12: {'points_mean': 14.35064935064935, 'duration_mean': 35.76623376623377},
                           'overall': {'points_mean': 13, 'duration_mean': 41}}
        # 'overall': {'points_mean': 12.843614718614718, 'duration_mean': 40.984307359307365}

    def step(self, action):
        if action not in [0, 1, 2, 3]:
            raise Exception('Action must be 0, 1, 2 or 3 (NONE, NOTIFICATION, SUGGESTION, INTERVENTION)')
        trust, points, duration = self.user_simulator.simulate(step_number=self.step_number, action=action)

        reward = 0
        reward += self.reward_table_trust[int(trust)]
        if int(points) == self.max_points[self.step_number - 1]:
            reward += self.reward_table_points['max']
        elif int(points) == 0:
            reward += self.reward_table_points['min']
        elif int(points) > self.mean_table[self.step_number]['points_mean']:
            reward += self.reward_table_points['>mean']
        elif int(points) < self.mean_table[self.step_number]['points_mean']:
            reward += self.reward_table_points['<mean']
        elif int(points) == self.mean_table[self.step_number]['points_mean']:
            reward += self.reward_table_points['mean']

        if int(duration) > self.mean_table[self.step_number]['duration_mean'] +2:
            reward += self.reward_table_duration['>mean']
        elif int(duration) < self.mean_table[self.step_number]['duration_mean']-2:
            reward += self.reward_table_duration['<mean']
        elif int(duration) <= self.mean_table[self.step_number]['duration_mean']+2 and int(duration) >= self.mean_table[self.step_number]['duration_mean']-2:
            reward += self.reward_table_duration['mean']

        self.step_number += 1

        observation = np.array(
            [(self.step_number-1)/11, (self.complexity_list[self.step_number - 1]-3)/2, (trust-1)/4, points/(self.max_points[self.step_number - 2]), (duration-20)/880]).astype(np.float32)

        done = bool(self.step_number == 13)
        info = {}

        return observation, reward, done, info

    def reset(self):
        self.step_number = 1
        self.user_simulator.generate_person_data()
        trust = self.user_simulator.get_pretrust()
        return np.array([(self.step_number-1)/11, (self.complexity_list[self.step_number - 1]-3)/2, (trust-1)/4,
                         0,0]).astype(np.float32)
        # reward, done, info can't be included in the return of the reset function

    def render(self, mode='console'):
        pass

    def close(self):
        pass


class CustomUserSimulatorEnvComplexity(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['console']}

    NONE = 0
    NOTIFICATION = 1
    SUGGESTION = 2
    INTERVENTION = 3

    def __init__(self):
        super(CustomUserSimulatorEnvComplexity, self).__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=np.array([3, 1]),
                                            high=np.array([5, 5]),
                                            dtype=np.int16)  # complexity, trust (points)
        # self.user_simulator = us_dummy.DummyClass()
        self.user_simulator = user_simulator_com.UserSimulator()
        self.user_simulator.generate_person_data()

        self.step_number = 1
        self.complexity = [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]

        self.points = 0
        self.reward_table = {1: -20, 2: -10, 3: 0, 4: 10, 5: 20}

    def step(self, action):
        if action not in [0, 1, 2, 3]:
            raise Exception('Action must be 0, 1, 2 or 3 (NONE, NOTIFICATION, SUGGESTION, INTERVENTION)')
        complexity = self.complexity[self.step_number - 1]
        trust, points = self.user_simulator.simulate(step_number=self.step_number, complexity=complexity, action=action)

        done = bool(self.step_number == 12)
        observation = np.array([complexity, trust]).astype(np.int16)
        reward = self.reward_table[int(trust)]
        info = {}

        self.step_number += 1

        return observation, reward, done, info

    def reset(self):
        self.step_number = 1
        self.user_simulator.generate_person_data()
        trust = self.user_simulator.get_pretrust()
        complexity = self.complexity[self.step_number - 1]
        return np.array([complexity, trust]).astype(np.int16)  # reward, done, info can't be included

    def render(self, mode='console'):
        pass

    def close(self):
        pass


if __name__ == '__main__':
    env = CustomUserSimulatorEnvStepNumber()
    print(env.reset())
    print(type(env.reset()))
    for i in range(1, 13):
        ret = env.step(np.random.choice([0, 1, 2, 3]))
        print(ret)
        if ret[2]:
            print('-----')
            print(env.reset())

    check_env(env, warn=True)
    print('done')

    # env = CustomUserSimulatorEnvComplexity()
    # for i in range(1, 16):
    #     print(i)
    #     print(env.step(np.random.choice([0, 1, 2, 3])))
    #     if i == 12:
    #         env.reset()
    # check_env(env, warn=True)
    # print('done')

# Todo: import error fixen
