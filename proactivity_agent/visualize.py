import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

evaluation = np.load('trained_models/a2c/12_20_2021_18_05/logs/evaluations.npz')
print(evaluation)

df = pd.read_csv('trained_models/a2c/12_20_2021_18_05/logs/log/monitor.csv', skiprows=1)
print(df.columns)
rewards = df['r']
print(len(rewards.index))
new_rewards = rewards.groupby(np.arange(len(rewards)) // 64).mean().copy()
print(len(new_rewards.index))
plt.plot(new_rewards)
plt.title('a2c_old')
plt.show()

df = pd.read_csv('trained_models/ppo/12_20_2021_18_11/logs/log/monitor.csv', skiprows=1)
print(df.columns)
rewards = df['r']
print(len(rewards.index))
new_rewards = rewards.groupby(np.arange(len(rewards)) // 64).mean().copy()
print(len(new_rewards.index))
plt.plot(new_rewards)
plt.title('ppo_old')
plt.show()

df = pd.read_csv('trained_models/a2c/12_21_2021_23_21/logs/log/monitor.csv', skiprows=1)
print(df.columns)
rewards = df['r']
print(len(rewards.index))
new_rewards = rewards.groupby(np.arange(len(rewards)) // 64).mean().copy()
print(len(new_rewards.index))
plt.plot(new_rewards)
plt.title('a2c_new')
plt.show()

df = pd.read_csv('trained_models/ppo/12_21_2021_23_21/logs/log/monitor.csv', skiprows=1)
print(df.columns)
rewards = df['r']
print(len(rewards.index))
new_rewards = rewards.groupby(np.arange(len(rewards)) // 64).mean().copy()
print(len(new_rewards.index))
plt.plot(new_rewards)
plt.title('ppo_new')
plt.show()

df = pd.read_csv('trained_models/dqn/01_23_2022_17_55/logs/log/monitor.csv', skiprows=1)
print(df.columns)
rewards = df['r']
print(len(rewards.index))
new_rewards = rewards.groupby(np.arange(len(rewards)) // 64).mean().copy()
print(len(new_rewards.index))
plt.plot(new_rewards)
plt.title('dqn_new')
plt.show()

""" a2c_od: 200
    ppo_old: 215
    a2c_new: 190
    ppo_new: 230
    dqn_new: 235"""
