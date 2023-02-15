# python version 3.9
import pandas as pd
import numpy as np
from datetime import datetime
import os
import pickle
import configparser

from user_simulator.complexity_dependent import personalDetails
from user_simulator.complexity_dependent import simData
from user_simulator.complexity_dependent import genPoints
from user_simulator.complexity_dependent import createDataVector


class UserSimulator:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.pers_data_obj = personalDetails.PersonalDetails()  # Creates instance for generating the personal data
        self.step_data_obj = simData.SimData()  # Creates Object for generating the step data
        self.points_data_obj = genPoints.GenPoints()
        self.input_vector_obj = createDataVector.CreateDataVector()

        self.simulated_pers_data = {}
        self.simulated_step_data = {}
        self.simulated_points_data = {}

        self.last_trust = 0

        with open("user_simulator/complexity_dependent/svm_trust_Model.pkl", 'rb') as file:
            self.trust_estimator_model = pickle.load(file)

        self.simulated_data_temp = pd.DataFrame()

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

    def gen_pers_data(self):
        self.pers_data_obj.generate_person_data()
        self.simulated_pers_data = self.pers_data_obj.pers_data
        pers_data = self.pers_data_obj.pers_data

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

    def gen_step_data(self, complexity, proactivity, pers_data, step_number):
        self.step_data_obj.set_proactivity(proactivity=proactivity)
        self.step_data_obj.set_complexity(complexity=complexity)
        self.step_data_obj.generate_values(personality_values=pers_data)
        self.simulated_step_data = self.step_data_obj.simulated_step_data
        step_data = self.step_data_obj.simulated_step_data

        self.simulated_data_temp['pers_code'] = [step_data['pers_code']]
        self.simulated_data_temp['complexity' + str(step_number)] = [step_data['complexity']]
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

        self.simulated_data_temp['points' + str(step_number)] = [
            self.points_data_obj.simulated_step_data_points['points']]

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

    def generate_person_data(self):
        self.simulated_data_temp = pd.DataFrame()
        self.gen_pers_data()

    def get_pretrust(self):
        # self.last_trust = 1
        self.last_trust = self.simulated_data_temp.loc[(0, 'preTrust')]
        return self.last_trust

    def simulate(self, step_number, complexity, action):
        proactivity = [1, 0, 0, 0]
        if action == 0:
            proactivity = [1, 0, 0, 0]
        elif action == 1:
            proactivity = [0, 1, 0, 0]
        elif action == 2:
            proactivity = [0, 0, 1, 0]
        elif action == 3:
            proactivity = [0, 0, 0, 1]

        self.simulated_data_temp['proactivity' + str(step_number)] = [self.proactivity_encoding_to_text(proactivity)]

        self.gen_step_data(complexity=str(complexity), proactivity=proactivity, pers_data=self.simulated_pers_data,
                           step_number=step_number)
        self.gen_points_data(step_number=step_number, sim_step_data=self.simulated_step_data)
        self.estimate_trust(step_number=step_number)

        return self.simulated_data_temp.loc[(0, 'trust' + str(step_number))], self.simulated_data_temp.loc[
            (0, 'points' + str(step_number))]


if __name__ == '__main__':
    t1 = datetime.now()
    obj = UserSimulator()
    obj.generate_person_data()
    for u, r in zip((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), (3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5)):
        trust, points = obj.simulate(step_number=u, complexity=r, action=np.random.choice([0, 1, 2, 3, 4]))
        print('step: ', u, r, 'trust: ', trust, ' | points: ', points)

    print(obj.simulated_data_temp.to_string())
    t2 = datetime.now()
    print('time: ', t2 - t1)

    # TODO Abhängigkeit der Punkte
    # TODO Kommazahlen raus nehmen
    # TODO mehr Abhängigkeiten
