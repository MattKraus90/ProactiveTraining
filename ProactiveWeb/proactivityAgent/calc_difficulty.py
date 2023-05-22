import os

import numpy as np
import pandas as pd
from utils import write_json

DIRECTORY_PATH = os.path.dirname(__file__)

if __name__ == "__main__":
    df_whole = pd.read_csv(os.path.join(
        DIRECTORY_PATH, 'data/dataSummary.csv'))
    df_whole = df_whole.reindex(sorted(df_whole.columns), axis=1)
    df_dict = df_whole.to_dict()

    difficulties = {}

    difficultyTask = np.fromiter(
        df_dict['difficultyTask1'].values(), dtype=int)
    difficulties['1'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask2'].values(), dtype=int)
    difficulties['2'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask3'].values(), dtype=int)
    difficulties['3'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask4'].values(), dtype=int)
    difficulties['4'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask5'].values(), dtype=int)
    difficulties['5'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask6'].values(), dtype=int)
    difficulties['6'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask7'].values(), dtype=int)
    difficulties['7'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask8'].values(), dtype=int)
    difficulties['8'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask9'].values(), dtype=int)
    difficulties['9'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask10'].values(), dtype=int)
    difficulties['10'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask11'].values(), dtype=int)
    difficulties['11'] = np.mean(difficultyTask)
    difficultyTask = np.fromiter(
        df_dict['difficultyTask12'].values(), dtype=int)
    difficulties['12'] = np.mean(difficultyTask)

    path = os.path.join(DIRECTORY_PATH, 'data/difficulties.json')
    write_json(path, difficulties)

    print("done")
