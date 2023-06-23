import os

import numpy as np
import pandas as pd
from utils import write_json

DIRECTORY_PATH = os.path.dirname(__file__)

"""
file for calculating the mean of every tasks difficulty
only has to be run, when something changes
"""

if __name__ == "__main__":
    df_whole = pd.read_csv(os.path.join(
        DIRECTORY_PATH, 'data/dataSummary.csv'))
    df_whole = df_whole.reindex(sorted(df_whole.columns), axis=1)
    df_dict = df_whole.to_dict()

    difficulties = {}

    for i in range(1, 13):
        difficultyTask = np.fromiter(
            df_dict[f'difficultyTask{i}'].values(), dtype=int)
        difficulties[str(i)] = np.mean(difficultyTask)

    path = os.path.join(DIRECTORY_PATH, 'data/difficulties.json')
    write_json(path, difficulties)

    print("done")
