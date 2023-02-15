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

        df = pd.read_csv('dataSummary.csv')
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


if __name__ == '__main__':
    from io import StringIO
    import pickle

    with open("misc/Trust-Schätzer/svm_trust_Model.pkl", 'rb') as file:
        Pickled_LR_Model = pickle.load(file)

    #     TESTDATA = StringIO(""",age,gender,technical affinity,management experience,preTrust,neuroticism,extraversion,openness,agreeableness,conscientiousness,pers_code,complexity1,proactivity1,helpRequest1,suggestionRequest1,duration1,difficulty1,points1,complexity2,proactivity2,helpRequest2,suggestionRequest2,duration2,difficulty2,points2,complexity3,proactivity3,helpRequest3,suggestionRequest3,duration3,difficulty3,points3,complexity4,proactivity4,helpRequest4,suggestionRequest4,duration4,difficulty4,points4,complexity5,proactivity5,helpRequest5,suggestionRequest5,duration5,difficulty5,points5,complexity6,proactivity6,helpRequest6,suggestionRequest6,duration6,difficulty6,points6,complexity7,proactivity7,helpRequest7,suggestionRequest7,duration7,difficulty7,points7,complexity8,proactivity8,helpRequest8,suggestionRequest8,duration8,difficulty8,points8,complexity9,proactivity9,helpRequest9,suggestionRequest9,duration9,difficulty9,points9,complexity10,proactivity10,helpRequest10,suggestionRequest10,duration10,difficulty10,points10,complexity11,proactivity11,helpRequest11,suggestionRequest11,duration11,difficulty11,points11,complexity12,proactivity12,helpRequest12,suggestionRequest12,duration12,difficulty12,points12,#duration,#points
    # 0,41.85,female,4.71,1.33,3.14,2.8,4.59,3.22,1.72,2.97,011,3,notification,0,0,22.33,1.89,10,4,notification,0,0,32.41,3.39,10,5,intervention,0,0,44.79,3.36,10,3,suggestion,0,0,40.73,1.88,10,4,intervention,0,0,36.8,1.6,10,5,intervention,0,0,21.58,1.94,20,3,notification,0,0,23.27,3.42,20,4,intervention,1,0,41.49,2.51,20,5,notification,1,0,43.64,1.75,40,3,intervention,0,0,77.29,2.75,10,4,notification,0,0,44.98,3.38,10,5,suggestion,0,0,40.87,1.98,20,470.18,190
    # """)

    TESTDATA = StringIO(""",age,gender,technical affinity,management experience,preTrust,neuroticism,extraversion,openness,agreeableness,conscientiousness,pers_code,complexity1,proactivity1,helpRequest1,suggestionRequest1,duration1,difficulty1,points1,trust1,complexity2,proactivity2,helpRequest2,suggestionRequest2,duration2,difficulty2,points2,trust2,complexity3,proactivity3,helpRequest3,suggestionRequest3,duration3,difficulty3,points3,trust3,complexity4,proactivity4,helpRequest4,suggestionRequest4,duration4,difficulty4,points4,trust4,complexity5,proactivity5,helpRequest5,suggestionRequest5,duration5,difficulty5,points5,trust5,complexity6,proactivity6,helpRequest6,suggestionRequest6,duration6,difficulty6,points6,trust6,complexity7,proactivity7,helpRequest7,suggestionRequest7,duration7,difficulty7,points7,trust7,complexity8,proactivity8,helpRequest8,suggestionRequest8,duration8,difficulty8,points8,trust8,complexity9,proactivity9,helpRequest9,suggestionRequest9,duration9,difficulty9,points9,trust9,complexity10,proactivity10,helpRequest10,suggestionRequest10,duration10,difficulty10,points10,trust10,complexity11,proactivity11,helpRequest11,suggestionRequest11,duration11,difficulty11,points11,trust11,complexity12,proactivity12,helpRequest12,suggestionRequest12,duration12,difficulty12,points12,trust12,#duration,#points
0,20,male,3.47,3.79,3.47,3.81,2.84,4.86,4.23,4.11,111,3,none,0,1,34.84,5,10,1,4,suggestion,0,0,38.51,4,10,1,5,none,0,1,36.23,4,0,1,3,none,0,1,31.1,4,10,1,4,none,0,1,40.3,2,0,1,5,none,0,1,27.52,1,20,1,3,none,0,1,34.21,2,10,1,4,none,0,1,23.11,3,20,1,5,notification,0,0,32.31,2,10,1,3,intervention,0,0,27.65,4,10,1,4,none,0,1,25.14,3,10,1,5,intervention,0,0,25.9,4,10,1,604.14,110
""")

    test_obj = CreateDataVector()
    dataf = pd.read_csv(TESTDATA)
    # print(dataf)
    test_obj.load_current_dataframe(dataf)
    for i in range(1, 13):
        res = test_obj.create_vector(i)
        print(res)
        # print(len(res))
        result = Pickled_LR_Model.predict([res])
        print(int(result[0]))
        print()
