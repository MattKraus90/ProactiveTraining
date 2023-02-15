import json
import os
import numpy as np
import pandas as pd
from scipy import stats


class PersonalDetails:
    def __init__(self):
        # TODO: Aufräumen: objektvariablen raus und nur noch über dict arbeiten
        self.mean_age = 0.0
        self.std_age = 0.0
        self.prob_gender_male = 0.0
        self.prob_gender_female = 0.0
        self.prob_gender_other = 0.0
        self.mean_technaff = 0.0
        self.std_technaff = 0.0
        self.mean_managexp = 0.0
        self.std_managexp = 0.0
        self.mean_pretrust = 0.0
        self.std_pretrust = 0.0
        self.mean_neuroticism = 0.0
        self.std_neuroticism = 0.0
        self.mean_extraversion = 0.0
        self.std_extraversion = 0.0
        self.mean_openness = 0.0
        self.std_openness = 0.0
        self.mean_agreeableness = 0.0
        self.std_agreeableness = 0.0
        self.mean_conscientiousness = 0.0
        self.std_conscientiousness = 0.0

        self.dist_values = {'age': {'mean': 0.0, 'std': 0.0},
                            'gender': {'gender_male': 0.0, 'gender_female': 0.0, 'gender_other': 0.0},
                            'technical affinity': {'mean': 0.0, 'std': 0.0},
                            'management experience': {'mean': 0.0, 'std': 0.0},
                            'preTrust': {'mean': 0.0, 'std': 0.0},
                            'neuroticism': {'mean': 0.0, 'std': 0.0},
                            'extraversion': {'mean': 0.0, 'std': 0.0},
                            'openness': {'mean': 0.0, 'std': 0.0},
                            'agreeableness': {'mean': 0.0, 'std': 0.0},
                            'conscientiousness': {'mean': 0.0, 'std': 0.0}}

        try:
            file = open('user_simulator/complexity_dependent/user_simulator_data/dist_data/dist_data_personality.json', 'r')
            self.dist_values = json.load(file)
            print('Personality distribution values loaded from file...')
            self.save_dict_values_to_object_variables()

        except FileNotFoundError:
            print('Distribution data missing. (personal)')

        self.pers_data = {'age': 0.0, 'gender': '', 'technical affinity': 0.0, 'management experience': 0.0,
                          'preTrust': 0.0, 'neuroticism': 0.0, 'extraversion': 0.0, 'openness': 0.0,
                          'agreeableness': 0.0, 'conscientiousness': 0.0}

    def save_dict_values_to_object_variables(self):
        self.mean_age = self.dist_values['age']['mean']
        self.std_age = self.dist_values['age']['std']
        self.mean_technaff = self.dist_values['technical affinity']['mean']
        self.std_technaff = self.dist_values['technical affinity']['std']
        self.mean_managexp = self.dist_values['management experience']['mean']
        self.std_managexp = self.dist_values['management experience']['std']
        self.mean_pretrust = self.dist_values['preTrust']['mean']
        self.std_pretrust = self.dist_values['preTrust']['std']
        self.prob_gender_male = self.dist_values['gender']['gender_male']
        self.prob_gender_female = self.dist_values['gender']['gender_female']
        self.prob_gender_other = self.dist_values['gender']['gender_other']

        self.mean_neuroticism = self.dist_values['neuroticism']['mean']
        self.std_neuroticism = self.dist_values['neuroticism']['std']
        self.mean_extraversion = self.dist_values['extraversion']['mean']
        self.std_extraversion = self.dist_values['extraversion']['std']
        self.mean_openness = self.dist_values['openness']['mean']
        self.std_openness = self.dist_values['openness']['std']
        self.mean_agreeableness = self.dist_values['agreeableness']['mean']
        self.std_agreeableness = self.dist_values['agreeableness']['std']
        self.mean_conscientiousness = self.dist_values['conscientiousness']['mean']
        self.std_conscientiousness = self.dist_values['conscientiousness']['std']

    def load_distribution_parameter(self):
        """calculates the needed distribution values (e. g. mean, standard deviation) from data"""
        df = pd.read_csv('dataSummary.csv')

        df = df.reindex(sorted(df.columns), axis=1)

        self.mean_age = np.mean(df['Age'])
        self.std_age = np.std(df['Age'])

        self.mean_technaff = np.mean(df['Technical Affinity'])
        self.std_technaff = np.std(df['Technical Affinity'])

        self.mean_managexp = np.mean(df['ExperienceManagement'])
        self.std_managexp = np.std(df['ExperienceManagement'])

        self.mean_pretrust = np.mean(df['PreTrust'])
        self.std_pretrust = np.std(df['PreTrust'])

        gender_counts = df['Gender'].value_counts()
        gender_counts_sum = df['Gender'].value_counts().sum(axis=0)
        self.prob_gender_male = gender_counts['male'] / gender_counts_sum
        self.prob_gender_female = gender_counts['female'] / gender_counts_sum
        self.prob_gender_other = gender_counts['other'] / gender_counts_sum

        self.mean_neuroticism = np.mean(df['Neuroticism'])
        self.std_neuroticism = np.std(df['Neuroticism'])

        self.mean_extraversion = np.mean(df['Extraversion'])
        self.std_extraversion = np.std(df['Extraversion'])

        self.mean_openness = np.mean(df['Openness'])
        self.std_openness = np.std(df['Openness'])

        self.mean_agreeableness = np.mean(df['Agreeableness'])
        self.std_agreeableness = np.std(df['Agreeableness'])

        self.mean_conscientiousness = np.mean(df['Conscientiousness'])
        self.std_conscientiousness = np.std(df['Conscientiousness'])

        self.dist_values['age']['mean'] = float(self.mean_age)
        self.dist_values['age']['std'] = float(self.std_age)
        self.dist_values['technical affinity']['mean'] = float(self.mean_technaff)
        self.dist_values['technical affinity']['std'] = float(self.std_technaff)
        self.dist_values['management experience']['mean'] = float(self.mean_managexp)
        self.dist_values['management experience']['std'] = float(self.std_managexp)
        self.dist_values['preTrust']['mean'] = float(self.mean_pretrust)
        self.dist_values['preTrust']['std'] = float(self.std_pretrust)
        self.dist_values['gender']['gender_male'] = self.prob_gender_male
        self.dist_values['gender']['gender_female'] = self.prob_gender_female
        self.dist_values['gender']['gender_other'] = self.prob_gender_other

        self.dist_values['neuroticism']['mean'] = float(self.mean_neuroticism)
        self.dist_values['neuroticism']['std'] = float(self.std_neuroticism)
        self.dist_values['extraversion']['mean'] = float(self.mean_extraversion)
        self.dist_values['extraversion']['std'] = float(self.std_extraversion)
        self.dist_values['openness']['mean'] = float(self.mean_openness)
        self.dist_values['openness']['std'] = float(self.std_openness)
        self.dist_values['agreeableness']['mean'] = float(self.mean_agreeableness)
        self.dist_values['agreeableness']['std'] = float(self.std_agreeableness)
        self.dist_values['conscientiousness']['mean'] = float(self.mean_conscientiousness)
        self.dist_values['conscientiousness']['std'] = float(self.std_conscientiousness)

    def gen_age(self):
        """generates a random value for age"""
        lower = 18.0
        # self.pers_data['age'] = float(
        #     np.around(np.random.normal(loc=self.mean_age, scale=self.std_age, size=1), decimals=0))
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_age) / self.std_age, np.inf, loc=self.mean_age,
            scale=self.std_age)
        self.pers_data['age'] = float(np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_gender(self):
        """generates a random value for gender"""
        self.pers_data['gender'] = str(np.random.choice(['male', 'female', 'other'],
                                                        p=[self.prob_gender_male, self.prob_gender_female,
                                                           self.prob_gender_other], size=1)[0])

    def gen_technaff(self):
        """generates a random value for technical affinity"""
        # self.pers_data['technical affinity'] = float(np.around(
        #     np.random.normal(loc=self.mean_technaff, scale=self.std_technaff, size=1), decimals=0))
        lower, upper = 1, 5
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_technaff) / self.std_technaff, (upper - self.mean_technaff) / self.std_technaff,
            loc=self.mean_technaff, scale=self.std_technaff)
        self.pers_data['technical affinity'] = float(
            np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_managexp(self):
        """generates a random value for management experience"""
        # self.pers_data['management experience'] = float(np.around(
        #     np.random.normal(loc=self.mean_managexp, scale=self.std_managexp,
        #                      size=1), decimals=0))
        lower, upper = 1, 5
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_managexp) / self.std_managexp, (upper - self.mean_managexp) / self.std_managexp,
            loc=self.mean_managexp, scale=self.std_managexp)
        self.pers_data['management experience'] = float(
            np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_pretrust(self):
        """generates a random value for pretrust"""
        # self.pers_data['preTrust'] = float(np.around(
        #     np.random.normal(loc=self.mean_pretrust, scale=self.std_pretrust, size=1), decimals=0))
        lower, upper = 1, 5
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_pretrust) / self.std_pretrust, (upper - self.mean_pretrust) / self.std_pretrust,
            loc=self.mean_pretrust, scale=self.std_pretrust)
        self.pers_data['preTrust'] = float(
            np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_neuroticism(self):
        """generates a random value for neuroticism"""
        # self.pers_data['neuroticism'] = float(np.around(
        #     np.random.normal(loc=self.mean_neuroticism, scale=self.std_neuroticism, size=1), decimals=0))
        lower, upper = 1, 5
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_neuroticism) / self.std_neuroticism,
            (upper - self.mean_neuroticism) / self.std_neuroticism,
            loc=self.mean_neuroticism, scale=self.std_neuroticism)
        self.pers_data['neuroticism'] = float(
            np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_extraversion(self):
        """generates a random value for extraversion"""
        # self.pers_data['extraversion'] = float(np.around(
        #     np.random.normal(loc=self.mean_extraversion, scale=self.std_extraversion, size=1), decimals=0))
        lower, upper = 1, 5
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_extraversion) / self.std_extraversion,
            (upper - self.mean_extraversion) / self.std_extraversion,
            loc=self.mean_extraversion, scale=self.std_extraversion)
        self.pers_data['extraversion'] = float(
            np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_openness(self):
        """generates a random value for openness"""
        # self.pers_data['openness'] = float(np.around(
        #     np.random.normal(loc=self.mean_openness, scale=self.std_openness, size=1), decimals=0))
        lower, upper = 1, 5
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_openness) / self.std_openness, (upper - self.mean_openness) / self.std_openness,
            loc=self.mean_openness, scale=self.std_openness)
        self.pers_data['openness'] = float(
            np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_agreeableness(self):
        """generates a random value for agreeableness"""
        # self.pers_data['agreeableness'] = float(np.around(
        #     np.random.normal(loc=self.mean_agreeableness, scale=self.std_agreeableness, size=1), decimals=0))
        lower, upper = 1, 5
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_agreeableness) / self.std_agreeableness,
            (upper - self.mean_agreeableness) / self.std_agreeableness,
            loc=self.mean_agreeableness, scale=self.std_agreeableness)
        self.pers_data['agreeableness'] = float(
            np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_conscientiousness(self):
        """generates a random value for conscientiousness"""
        # self.pers_data['conscientiousness'] = float(np.around(
        #     np.random.normal(loc=self.mean_conscientiousness, scale=self.std_conscientiousness, size=1), decimals=0))
        lower, upper = 1, 5
        truncated_norm_dist = stats.truncnorm(
            (lower - self.mean_conscientiousness) / self.std_conscientiousness,
            (upper - self.mean_conscientiousness) / self.std_conscientiousness,
            loc=self.mean_conscientiousness, scale=self.std_conscientiousness)
        self.pers_data['conscientiousness'] = float(
            np.around(truncated_norm_dist.rvs(1), decimals=0))

    def generate_person_data(self):
        self.gen_age()
        self.gen_gender()
        self.gen_technaff()
        self.gen_managexp()
        self.gen_pretrust()
        self.gen_neuroticism()
        self.gen_extraversion()
        self.gen_openness()
        self.gen_agreeableness()
        self.gen_conscientiousness()
        # print(self.pers_data)

    def generate_bunch_of_people(self, number):
        bunch_of_people = pd.DataFrame()

        for i in range(0, number):
            self.generate_person_data()

            temp = pd.DataFrame()
            pers_data = self.pers_data.copy()

            temp['age'] = [pers_data['age']]
            temp['gender'] = [pers_data['gender']]
            temp['technical affinity'] = [pers_data['technical affinity']]
            temp['management experience'] = [pers_data['management experience']]
            temp['preTrust'] = [pers_data['preTrust']]
            temp['neuroticism'] = [pers_data['neuroticism']]
            temp['extraversion'] = [pers_data['extraversion']]
            temp['openness'] = [pers_data['openness']]
            temp['agreeableness'] = [pers_data['agreeableness']]
            temp['conscientiousness'] = [pers_data['conscientiousness']]

            bunch_of_people = bunch_of_people.append(temp)

        try:
            os.makedirs("user_simulator_data/simulated_data/people")
        except FileExistsError:
            pass

        bunch_of_people = bunch_of_people.reset_index().drop(['index'], axis=1)
        bunch_of_people.to_csv('user_simulator_data/simulated_data/people/people.csv')


if __name__ == '__main__':
    # df1 = pd.read_csv('dataSummary.csv')
    #
    # df1 = df1.reindex(sorted(df1.columns), axis=1)
    #
    # # print(df1.head())
    # # print(df1['Age'])
    # print(df1['Gender'].value_counts())
    # v = df1['Gender'].value_counts()
    # s = df1['Gender'].value_counts().sum(axis=0)
    # p1 = v['male'] / s
    # p2 = v['female'] / s
    # p3 = v['other'] / s
    # print(p1 + p2 + p3)
    # s = np.random.choice(['male', 'female', 'other'], p=[p1, p2, p3], size=308)
    # df2 = pd.Series(s)
    # print(df2.value_counts())

    pD = PersonalDetails()
    # print(pD.dist_values)
    # pD.generate_bunch_of_people(1000)
    max_age = 0
    for i in range(100000):
        pD.gen_age()
        print(pD.pers_data['age'])
        if pD.pers_data['age'] > max_age:
            max_age = pD.pers_data['age']

    print('max_age', max_age)

