import os
import pickle

import numpy as np
import pandas as pd
from stable_baselines3 import DQN

from proactivityAgent.createDataVector import CreateDataVector
from proactivityAgent.createStepData import StepData
from proactivityAgent.personalDetails import PersonalDetails
from proactivityAgent.utils import proactivity_encoding_to_text, proactivity_text_to_encoding
from configparser import ConfigParser

DIRECTORY_PATH = os.path.dirname(__file__)

class ProactivityAgent:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
            cls._instance.config = ConfigParser()
            cls._instance.config.read(os.path.join(DIRECTORY_PATH, "data/Config.ini"))
            
            cls._instance.pers_data_obj = PersonalDetails()
            cls._instance.step_data_obj = StepData()
            cls._instance.input_vector_obj = CreateDataVector()
            
            cls._instance.pers_data = {}
            cls._instance.step_data = {}
            
            cls._instance.data = pd.DataFrame()
            cls._instance.data_temp = pd.DataFrame()        
            
            with open(os.path.join(DIRECTORY_PATH, "trust_model/svm_trust_Model.pkl"), 'rb') as file:
                cls._instance.trust_estimator_model = pickle.load(file)
            
            cls._instance.complexity_list = np.array([3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5])
            cls._instance.proactivity_agent_model = DQN.load(os.path.join(DIRECTORY_PATH, "agents/dqn_agent"))
            
            cls._instance.strategy_1_list = cls._instance.__get_strategy_1_list()
            
        return cls._instance

    def __get_strategy_1_list(self):
        if self.config['Proactivity_Strategy']['Strategy_1']:
            proactivity_steps = [np.random.choice([1, 2, 3]),
                                    np.random.choice([4, 5, 6]),
                                    np.random.choice([7, 8, 9]),
                                    np.random.choice([10, 11, 12])]
        else:
            proactivity_steps = []
        
        return proactivity_steps

    def __get_step_data(self):
        self.step_data_obj.set_step_data(self.step_number, self.proactivity, self.help_req, self.sugg_req, self.duration)
        self.step_data_obj.get_step_data(self.pers_data)
        self.step_data = self.step_data_obj.step_data

        self.data_temp['pers_code'] = [self.step_data['pers_code']]
        self.data_temp['step_number' + str(self.step_number)] = [self.step_data['step_number']]
        self.data_temp['proactivity' + str(self.step_number)] = [
            proactivity_encoding_to_text(self.step_data['proactivity'])]
        self.data_temp['helpRequest' + str(self.step_number)] = [self.step_data['helpRequest']]
        self.data_temp['suggestionRequest' + str(self.step_number)] = [self.step_data['suggestionRequest']]
        self.data_temp['duration' + str(self.step_number)] = [self.step_data['duration']]
        self.data_temp['difficulty' + str(self.step_number)] = [self.step_data['difficulty']]
    
    
    def __get_points_data(self):
        self.data_temp['points' + str(self.step_number)] = self.points
    
    
    def __estimate_trust(self, step_number):
        self.input_vector_obj.load_current_dataframe(self.data_temp)
        input_vector = self.input_vector_obj.create_vector(step_number)
        result = self.trust_estimator_model.predict([input_vector])
        self.last_trust = int(result[0])
        self.data_temp['trust' + str(step_number)] = int(result[0])
        

    def get_pers_data(self, pers_data_dict):
        self.pers_data = self.pers_data_obj.generate_person_data(pers_data_dict)
        
        self.data_temp['age'] = [self.pers_data['age']]
        self.data_temp['gender'] = [self.pers_data['gender']]
        self.data_temp['technical affinity'] = [self.pers_data['technical affinity']]
        self.data_temp['management experience'] = [self.pers_data['management experience']]
        self.data_temp['preTrust'] = [self.pers_data['preTrust']]
        self.data_temp['neuroticism'] = [self.pers_data['neuroticism']]
        self.data_temp['extraversion'] = [self.pers_data['extraversion']]
        self.data_temp['openness'] = [self.pers_data['openness']]
        self.data_temp['agreeableness'] = [self.pers_data['agreeableness']]
        self.data_temp['conscientiousness'] = [self.pers_data['conscientiousness']]
        
        
    def return_proactivity(self, step_number):
        if self.config['Proactivity_Strategy']['Just_one'] != 'False':
            self.proactivity = proactivity_text_to_encoding(self.config['Proactivity_Strategy']['just_one'])
        elif self.config['Proactivity_Strategy']['Random'] == 'True':
            self.proactivity = np.random.choice([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        elif self.config['Proactivity_Strategy']['Strategy_1'] == 'True':
            if step_number in self.strategy_1_list:
                self.proactivity = np.random.choice([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            else:
                self.proactivity = [1, 0, 0, 0] 
        # elif self.config['Proactivity_Strategy']['Strategy_Gt_Dataset'] == 'True':
        #     proactivity_df = pd.read_csv('../misc/DataAnalysis/proactivity_gt.csv')
        #     self.proactivity = proactivity_text_to_encoding(
        #         # TODO: user number
        #         proactivity_df.loc[user_number, 'ProactiveTask' + str(step_number)].lower())
        elif self.config['Proactivity_Strategy']['Strategy_Adaptive'] == 'True':
            if self.last_trust == 5:
                self.proactivity = [0, 0, 0, 1]
            elif self.last_trust == 4:
                self.proactivity = [0, 0, 1, 0]
            elif self.last_trust == 3:
                self.proactivity = [0, 1, 0, 0]
            else:
                self.proactivity = [1, 0, 0, 0]
        elif self.config['Proactivity_Strategy']['Strategy_agent'] == 'True':
            if step_number == 1:
                previous_duration = 35.76623376623377  # overall mean
                previous_points = 14.35064935064935  # overall mean
                previous_trust = self.data_temp.loc[(0, 'preTrust')]
            else:
                previous_duration = self.data_temp.loc[(0, 'duration' + str(step_number - 1))]
                previous_points = self.data_temp.loc[(0, 'points' + str(step_number - 1))]
                previous_trust = self.data_temp.loc[(0, 'trust' + str(step_number - 1))]

            observation = np.array([step_number, self.complexity_list[step_number - 1], previous_trust, previous_points,
                                    previous_duration]).astype(np.int16)
            action, _states = self.proactivity_agent_model.predict(observation, deterministic=True)
            
            if action == 3:
                self.proactivity = [0, 0, 0, 1]
            elif action == 2:
                self.proactivity = [0, 0, 1, 0]
            elif action == 1:
                self.proactivity = [0, 1, 0, 0]
            else:
                self.proactivity = [1, 0, 0, 0]
        else:
            raise Exception('Please choose a valid proactivity strategy.')
        
        return self.proactivity

        
    def calc_data(self, step_number, help_req, sugg_req, duration, points):
        self.step_number = step_number
        self.help_req = help_req
        self.sugg_req = sugg_req
        self.duration = duration
        self.points = points
        
        self.__get_step_data()
        self.__get_points_data()
        self.__estimate_trust(step_number)
        
        print(f"Step{step_number}  -->  helpRequest: {help_req} | suggestionReqest: {sugg_req} | "
              f"duration: {duration} | difficulty: {self.data_temp['difficulty' + str(self.step_number)][0]} | "
              f"proactivity: {proactivity_encoding_to_text(self.proactivity)} | step_number: {step_number} | "
              f"pers_code: {self.data_temp['pers_code'][0]} | points: {points} | "
              f"trust: {self.data_temp['trust' + str(step_number)][0]}")
        print()
