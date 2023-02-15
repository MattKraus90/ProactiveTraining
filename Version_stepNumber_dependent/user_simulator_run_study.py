# python version 3.9
import pandas as pd
import numpy as np
from datetime import datetime
import os
import pickle
import configparser
from stable_baselines3 import A2C, PPO, DQN

import personalDetails
import simData
import genPoints
import createDataVector

config = configparser.ConfigParser()
config.read('Config.ini')


class UserSimulator:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.pers_data_obj = personalDetails.PersonalDetails()  # Creates instance for generating the personal data
        self.step_data_obj = simData.SimData()  # Creates Object for generating the step data
        self.points_data_obj = genPoints.GenPoints()
        self.input_vector_obj = createDataVector.CreateDataVector()

        self.simulated_step_data = {}
        self.simulated_points_data = {}
        self.currentComplexity = 0
        self.max_points = [10, 10, 10, 10, 10, 30, 30, 20, 40, 20, 10, 20]
        self.bunch_of_people = pd.DataFrame()
        self.last_trust = 0

        with open("svm_trust_Model.pkl", 'rb') as file:
            self.trust_estimator_model = pickle.load(file)

        self.simulated_data = pd.DataFrame()
        self.simulated_data_temp = pd.DataFrame()

        self.proactivity_strategies_dict = {1: 'only_none', 2: 'only_notification', 3: 'only_suggestion',
                                            4: 'only_intervention', 5: 'adaptive_strategy', 6: 'proactivity_agent', 7: 'random'}

        self.complexity_list = [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]
        # self.proactivity_agent_model = A2C.load('agents/a2c_agent.zip')
        #self.proactivity_agent_model = PPO.load('agents/ppo_agent.zip')
        self.proactivity_agent_model = DQN.load('agents/dqn_proactivity_agent_optimised.zip')

    @staticmethod
    def proactivity_encoding_to_text(proactivity):
        if proactivity == [1, 0, 0, 0]:
            return 'none'
        elif proactivity == [0, 1, 0, 0]:
            return 'notification'
        elif proactivity == [0, 0, 1, 0]:
            return 'suggestion'
        elif proactivity == [0, 0, 0, 1]:
            return 'intervention'

    @staticmethod
    def proactivity_text_to_encoding(proactivity):
        if proactivity == 'none':
            return [1, 0, 0, 0]
        elif proactivity == 'notification':
            return [0, 1, 0, 0]
        elif proactivity == 'suggestion':
            return [0, 0, 1, 0]
        elif proactivity == 'intervention':
            return [0, 0, 0, 1]

    def generate_bunch_of_people(self, number):
        bunch_of_people = pd.DataFrame()

        for i in range(0, number):
            self.pers_data_obj.generate_person_data()

            temp = pd.DataFrame()
            pers_data = self.pers_data_obj.pers_data

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

        self.bunch_of_people = bunch_of_people.reset_index().drop(['index'], axis=1)
        # try:
        #     os.makedirs("user_simulator_data/simulated_data/people")
        # except FileExistsError:
        #     pass
        # self.bunch_of_people.to_csv('user_simulator_data/simulated_data/people/people.csv')

    def save_pers_data(self, pers_data):
        self.simulated_data_temp['age'] = [pers_data['age']]
        self.simulated_data_temp['gender'] = [pers_data['gender']]
        self.simulated_data_temp['technical affinity'] = [pers_data['technical affinity']]
        self.simulated_data_temp['management experience'] = [pers_data['management experience']]
        self.simulated_data_temp['preTrust'] = [pers_data['preTrust']]
        self.simulated_data_temp['neuroticism'] = [pers_data['neuroticism']]
        self.simulated_data_temp['extraversion'] = [pers_data['extraversion']]
        self.simulated_data_temp['openness'] = [pers_data['openness']]
        self.simulated_data_temp['agreeableness'] = [pers_data['agreeableness']]
        self.simulated_data_temp['conscientiousness'] = [pers_data['conscientiousness']]

    def gen_step_data(self, proactivity, pers_data, step_number):
        self.step_data_obj.set_proactivity(proactivity=proactivity)
        self.step_data_obj.set_step_number(step_number=str(step_number))
        self.step_data_obj.generate_values(personality_values=pers_data)
        self.simulated_step_data = self.step_data_obj.simulated_step_data
        step_data = self.step_data_obj.simulated_step_data

        self.simulated_data_temp['pers_code'] = [step_data['pers_code']]
        self.simulated_data_temp['step_number' + str(step_number)] = [step_data['step_number']]
        self.simulated_data_temp['proactivity' + str(step_number)] = [
            self.proactivity_encoding_to_text(step_data['proactivity'])]
        self.simulated_data_temp['helpRequest' + str(step_number)] = [step_data['helpRequest']]
        self.simulated_data_temp['suggestionRequest' + str(step_number)] = [step_data['suggestionRequest']]
        self.simulated_data_temp['duration' + str(step_number)] = [step_data['duration']]
        self.simulated_data_temp['difficulty' + str(step_number)] = [step_data['difficulty']]

        # self.simulated_data["step{:0>2}".format(self.step_counter)] = {
        #     'sim_data': self.step_data_obj.simulated_step_data.copy()}

    def gen_points_data(self, step_number, sim_step_data):
        self.points_data_obj.set_step_number(step_number=step_number)
        self.points_data_obj.generate_points(sim_step_data=sim_step_data)
        self.simulated_points_data = self.points_data_obj.simulated_step_data_points
        points_data = self.points_data_obj.simulated_step_data_points

        self.simulated_data_temp['points' + str(step_number)] = [points_data['points']]

    def sum_up_duration_points(self):
        li_duration = []
        li_points = []
        for i in range(1, 13):
            li_duration.append(self.simulated_data_temp.loc[(0, 'duration' + str(i))])
            li_points.append(self.simulated_data_temp.loc[(0, 'points' + str(i))])
        ar_duration = np.array(li_duration)
        ar_points = np.array(li_points)
        self.simulated_data_temp['#duration'] = np.around(ar_duration.sum(), decimals=2)
        self.simulated_data_temp['#points'] = ar_points.sum()

    def generate_input_vector(self, step_number):
        self.input_vector_obj.load_current_dataframe(self.simulated_data_temp)
        input_vector = self.input_vector_obj.create_vector(step_number)
        return input_vector

    def estimate_trust(self, step_number):
        input_vector = self.generate_input_vector(step_number=step_number)
        result = self.trust_estimator_model.predict([input_vector])
        self.last_trust = int(result[0])
        self.simulated_data_temp['trust' + str(step_number)] = int(result[0])
        # return result

    def return_proactivity(self, flow, step_number=0):
        if flow == 1:
            return [1, 0, 0, 0]
        elif flow == 2:
            return [0, 1, 0, 0]
        elif flow == 3:
            return [0, 0, 1, 0]
        elif flow == 4:
            return [0, 0, 0, 1]
        elif flow == 5:

            if self.currentComplexity == 3 or self.currentComplexity == 6 or self.currentComplexity == 9 or self.currentComplexity == 12:

                if self.last_trust == 5:
                    return [0, 0, 0, 1]
                elif self.last_trust == 4:
                    return [0, 0, 0, 1]
                elif self.last_trust == 3:
                    return [0, 1, 0, 0]
                elif self.last_trust == 2:
                    return [1, 0, 0, 0]
                else:
                    return [0, 0, 1, 0]
            elif self.currentComplexity == 2 or self.currentComplexity == 5 or self.currentComplexity == 8 or self.currentComplexity == 11:

                if self.last_trust == 5:
                    return [0, 1, 0, 0]
                elif self.last_trust == 4:
                    return [0, 0, 1, 0]
                elif self.last_trust == 3:
                    return [1, 0, 0, 0]
                elif self.last_trust == 2:
                    return [0, 1, 0, 0]
                else:
                    return [0, 0, 1, 0]
            elif self.currentComplexity == 1 or self.currentComplexity == 4 or self.currentComplexity == 7 or self.currentComplexity == 10:

                if self.last_trust == 5:
                    return [0, 0, 1, 0]
                elif self.last_trust == 4:
                    return [1, 0, 0, 0]
                elif self.last_trust == 3:
                    return [0, 0, 1, 0]
                elif self.last_trust == 2:
                    return [1, 0, 0, 0]
                else:
                    return [0, 0, 0, 1]
            """
            if self.last_trust == 5:
                return [0, 0, 0, 1]
            elif self.last_trust == 4:
                return [0, 0, 1, 0]
            elif self.last_trust == 3:
                return [0, 1, 0, 0]
            elif self.last_trust == 2:
                return [1, 0, 0, 0]
            else:
                return [1, 0, 0, 0]
            """
        elif flow == 6:
            if step_number == 1:
                previous_trust = self.simulated_data_temp.loc[(0, 'preTrust')]
                previous_duration = 0  # overall mean
                previous_points = 0  # overall mean
            else:
                previous_trust = self.simulated_data_temp.loc[(0, 'trust' + str(step_number - 1))]
                previous_duration = self.simulated_data_temp.loc[(0, 'duration' + str(step_number - 1))]
                previous_points = self.simulated_data_temp.loc[(0, 'points' + str(step_number - 1))]

            observation = np.array([(step_number-1)/11, (self.complexity_list[step_number-1]-3)/2, (previous_trust-1)/4, previous_points/(self.max_points[step_number - 1]), (previous_duration-20)/880]).astype(np.float32)

            action, _states = self.proactivity_agent_model.predict(observation, deterministic=True)
            if action == 3:
                return [0, 0, 0, 1]
            elif action == 2:
                return [0, 0, 1, 0]
            elif action == 1:
                return [0, 1, 0, 0]
            else:
                return [1, 0, 0, 0]

        elif flow == 7:
            p_temp = np.random.choice(['1000', '0100', '0010', '0001'])
            return [int(x) for x in p_temp]
        else:
            raise Exception('proactivity strategy error')

    def run_study(self):
        print('Start simulating...')
        print('Create people...')
        # self.generate_bunch_of_people(10)
        self.generate_bunch_of_people(int(config['run_study']['size_bunch_of_people']))
        print('People are created.')
        number_of_runs = len(self.bunch_of_people.index)
        for f in range(1, 8):   # auf 7 ändern, wenn agent dabei sein soll
            print('flow', str(f), 'Proactivity strategy:', self.proactivity_strategies_dict[f])
            for i in range(number_of_runs):
                print('user: ', str(i))

                self.save_pers_data(self.bunch_of_people.loc[i])

                self.last_trust = self.simulated_data_temp.loc[(0, 'preTrust')]

                self.simulated_data_temp['proactivity_strategy'] = self.proactivity_strategies_dict[f]

                for step_number in range(1, 13):
                    self.currentComplexity = step_number
                    proactivity = self.return_proactivity(flow=f, step_number=step_number)
                    self.gen_step_data(proactivity=proactivity, pers_data=self.bunch_of_people.loc[i],
                                       step_number=step_number)
                    self.gen_points_data(step_number=step_number, sim_step_data=self.simulated_step_data)
                    self.estimate_trust(step_number=step_number)
                    s = "Step{:0>2} -->   ".format(step_number)
                    for k, v in self.simulated_step_data.items():
                        if k == 'used_values':
                            pass
                        elif k == 'proactivity':
                            s += k + ':  ' + self.proactivity_encoding_to_text(v) + ' |  '
                        else:
                            s += k + ':  ' + str(v) + ' |  '
                    print(s + 'points:  ' + str(self.simulated_points_data['points']) + ' |  '
                          + 'trust:  ' + str(self.simulated_data_temp.loc[(0, 'trust' + str(step_number))]))
                self.sum_up_duration_points()
                print('#duration:  {} |  #points:  {}'.format(self.simulated_data_temp.loc[(0, '#duration')],
                                                              self.simulated_data_temp.loc[(0, '#points')]))
                self.simulated_data = self.simulated_data.append(self.simulated_data_temp)
                print()
                self.simulated_data_temp = pd.DataFrame()

        try:
            os.makedirs("user_simulator_data/simulated_data")
        except FileExistsError:
            # directory already exists
            pass
        self.simulated_data = self.simulated_data.reset_index().drop(['index'], axis=1)
        self.simulated_data.to_csv(
            "user_simulator_data/simulated_data/run_study_simulated_data_" + str(self.timestamp) + config['Default'][
                'File_name_addon'] + ".csv")

        self.sum_and_save_results()

    def sum_and_save_results(self):
        try:
            os.makedirs("user_simulator_data/results")
        except FileExistsError:
            # directory already exists
            pass

        results = pd.DataFrame(
            columns=['ProactivityStrategy', '#Duration', '#Points', '#HelpRequest', '#SuggestionRequest', 'mean_Trust',
                     'last_Trust'])

        length = len(self.simulated_data.index)
        for index, dialog in self.simulated_data.reindex(sorted(self.simulated_data.columns), axis=1).iterrows():
            if index % 20 == 0:
                print(index, 'from', length)

            results_temp = pd.DataFrame()
            # columns=['ProactivityStrategy', '#Duration', '#Points', '#HelpRequest', '#SuggestRequest', 'mean_Trust',
            #          'last_Trust'])
            results_temp['ProactivityStrategy'] = [dialog.get('proactivity_strategy')]
            results_temp['#Duration'] = [dialog.get('#duration')]
            results_temp['#Points'] = [dialog.get('#points')]
            results_temp['#HelpRequest'] = [dialog['helpRequest1':'helpRequest9'].sum()]
            results_temp['#SuggestionRequest'] = [dialog['suggestionRequest1':'suggestionRequest9'].sum()]
            results_temp['mean_Trust'] = [dialog['trust1':'trust9'].mean()]
            results_temp['last_Trust'] = [dialog.get('trust12')]

            results = results.append(results_temp)

        results = results.reset_index().drop(['index'], axis=1)

        results.to_csv(
            "user_simulator_data/results/run_study_step_number_results_" + str(self.timestamp) + config['Default'][
                'File_name_addon'] + ".csv")


if __name__ == '__main__':
    t1 = datetime.now()
    obj = UserSimulator()
    obj.run_study()
    t2 = datetime.now()
    print('time: ', t2 - t1)
    # proactivity = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    # step_number = ['3', '4', '5', '3']
    # for p, c in zip(proactivity, step_number):
    #     print(p, c)
    #     obj.gen_step_data(step_number=c, proactivity=p)

    # obj.gen_step_data(step_number='3', proactivity=[1, 0, 0, 0])

    # TODO Abhängigkeit der Punkte
    # TODO Kommazahlen raus nehmen
    # TODO mehr Abhängigkeiten
