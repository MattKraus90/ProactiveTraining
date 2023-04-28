import os

import numpy as np
import pandas as pd

# mean = 1
# std = 1
# mean_points = 1
# std_points = 1
# mean_likert = 1
# std_likert = 1
# duration_task_mean = [1]
# duration_task_std = [1]

DIRECTORY_PATH = os.path.dirname(__file__)

class CreateDataVector:
    def __init__(self):
        self.input_vector = []
        self.empty = np.zeros(15)
        self.dialogue_vector = []
        self.window_vector = []
        self.personal_vector = []
        self.current_dataframe = pd.DataFrame()

        e = np.array([0, 10, 20, 30, 40])
        self.mean_points = np.mean(e)
        self.std_points = np.std(e)

        a = np.array([1, 2, 3, 4, 5])

        self.mean_likert = np.mean(a)
        self.std_likert = np.std(a)

        df = pd.read_csv(os.path.join(DIRECTORY_PATH, 'data/dataSummary.csv'))
        df = df.reindex(sorted(df.columns), axis=1)

        self.mean_age = df['Age'].mean()
        self.std_age = df['Age'].std()

        self.duration_task_mean = []
        self.duration_task_std = []

        for task in range(1, 13):
            mean = df['TimeDurationTask' + str(task)].mean()
            std = df['TimeDurationTask' + str(task)].std()
            self.duration_task_mean.append(mean)
            self.duration_task_std.append(std)

    def load_current_dataframe(self, data):
        self.current_dataframe = data

    def create_current_task_features(self, step_number):
        current_task_vector = []
        if self.current_dataframe.loc[(0, 'proactivity' + str(step_number))] == 'none':
            current_task_vector.extend([1, 0, 0, 0])
        elif self.current_dataframe.loc[(0, 'proactivity' + str(step_number))] == 'notification':
            current_task_vector.extend([0, 1, 0, 0])
        elif self.current_dataframe.loc[(0, 'proactivity' + str(step_number))] == 'suggestion':
            current_task_vector.extend([0, 0, 1, 0])
        elif self.current_dataframe.loc[(0, 'proactivity' + str(step_number))] == 'intervention':
            current_task_vector.extend([0, 0, 0, 1])

        current_task_vector.append(
            (float(
                self.current_dataframe.loc[(0, 'difficulty' + str(step_number))]) - self.mean_likert) / self.std_likert)
        if step_number == 1 or 2 or 3 or 4 or 5 or 11:
            current_task_vector.append((10 - self.mean_points) / self.std_points)
        elif step_number == 8 or 10 or 12:
            current_task_vector.append((20 - self.mean_points) / self.std_points)
        elif step_number == 6 or 7:
            current_task_vector.append((30 - self.mean_points) / self.std_points)
        elif step_number == 9:
            current_task_vector.append((40 - self.mean_points) / self.std_points)

        if step_number == 1 or 4 or 7 or 10:
            current_task_vector.extend([1, 0, 0])
        elif step_number == 2 or 5 or 8 or 11:
            current_task_vector.extend([0, 1, 0])
        elif step_number == 3 or 6 or 9 or 12:
            current_task_vector.extend([0, 0, 1])

        if self.current_dataframe.loc[(0, 'suggestionRequest' + str(step_number))] == 1:
            current_task_vector.extend([1, 0])
        else:
            current_task_vector.extend([0, 1])

        if self.current_dataframe.loc[(0, 'helpRequest' + str(step_number))] == 1:
            current_task_vector.extend([1, 0])
        else:
            current_task_vector.extend([0, 1])

        # TODO: points nur in Window-Level und was ist mit mean und std
        current_task_vector.append(
            (self.current_dataframe.loc[(0, 'points' + str(step_number))] - self.mean_points) / self.std_points)

        current_task_vector.append(
            (self.current_dataframe.loc[(0, 'duration' + str(step_number))] - self.duration_task_mean[
                step_number - 1]) / self.duration_task_std[step_number - 1])

        return current_task_vector

    def create_dialogue_features(self, step_number):
        self.dialogue_vector = []
        if step_number == 1:
            self.dialogue_vector = self.empty
        else:
            added_up_features_array = np.array(self.create_current_task_features(step_number=step_number))
            for n in range(step_number - 1, 0, -1):
                added_up_features_array += self.create_current_task_features(n)
            self.dialogue_vector = added_up_features_array / step_number

    def create_window_features(self, step_number):
        self.window_vector = []
        if step_number < 3:
            self.window_vector = self.empty
        else:
            added_up_features_array = np.array(self.create_current_task_features(step_number=step_number))
            added_up_features_array += np.array(self.create_current_task_features(step_number=step_number - 1))
            added_up_features_array += np.array(self.create_current_task_features(step_number=step_number - 2))

            self.window_vector = added_up_features_array / 3

    def create_user_features(self):
        self.personal_vector = []
        self.personal_vector.append(
            (self.current_dataframe.loc[(0, 'technical affinity')] - self.mean_likert) / self.std_likert)
        self.personal_vector.append((self.current_dataframe.loc[(0, 'preTrust')] - self.mean_likert) / self.std_likert)
        # TODO: age nicht likert
        self.personal_vector.append((self.current_dataframe.loc[(0, 'age')] - self.mean_age) / self.std_age)

        if self.current_dataframe.loc[(0, 'gender')] == 'male':
            self.personal_vector.extend([1, 0, 0])
        if self.current_dataframe.loc[(0, 'gender')] == 'female':
            self.personal_vector.extend([0, 1, 0])
        if self.current_dataframe.loc[(0, 'gender')] == 'other':
            self.personal_vector.extend([0, 0, 1])

        self.personal_vector.append(
            (self.current_dataframe.loc[(0, 'management experience')] - self.mean_likert) / self.std_likert)
        self.personal_vector.append(
            (self.current_dataframe.loc[(0, 'neuroticism')] - self.mean_likert) / self.std_likert)
        self.personal_vector.append(
            (self.current_dataframe.loc[(0, 'extraversion')] - self.mean_likert) / self.std_likert)
        self.personal_vector.append((self.current_dataframe.loc[(0, 'openness')] - self.mean_likert) / self.std_likert)
        self.personal_vector.append(
            (self.current_dataframe.loc[(0, 'agreeableness')] - self.mean_likert) / self.std_likert)
        self.personal_vector.append(
            (self.current_dataframe.loc[(0, 'conscientiousness')] - self.mean_likert) / self.std_likert)

    def create_vector(self, step):
        self.input_vector = []
        self.create_window_features(step_number=step)
        self.create_dialogue_features(step_number=step)
        current_task_vector = self.create_current_task_features(step_number=step)
        self.create_user_features()

        self.input_vector.extend(self.window_vector)
        self.input_vector.extend(self.dialogue_vector)
        self.input_vector.extend(current_task_vector)
        self.input_vector.extend(self.personal_vector)
        # Todo: means und  stds berechnen und einfügen
        # print('window: ', self.window_vector)
        # print('dialogue: ', self.dialogue_vector)
        # print('current: ', current_task_vector)
        # print('personal: ', self.personal_vector)
        # print('lwindow: ', len(self.window_vector))
        # print('ldialogue: ', len(self.dialogue_vector))
        # print('lcurrent: ', len(current_task_vector))
        # print('lpersonal: ', len(self.personal_vector))
        # pass
        return self.input_vector
