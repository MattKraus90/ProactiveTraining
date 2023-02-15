import pandas as pd
import numpy as np
import json
import distributionParameterPoints


class GenPoints:
    def __init__(self):
        self.dist_parameter_points = {}
        self.proactivity = None
        self.step_number = None

        self.simulated_step_data_points = {'points': 0, 'step_number': 0, 'proactivity': '',
                                           'used_values': {'pers_code': '000', 'HelpSugg': ''}}

        try:
            file = open("user_simulator_data/dist_data/dist_data_points.json", 'r')
            self.dist_parameter_points = json.load(file)
            print("Points distribution values loaded from file...")

        except FileNotFoundError:
            print("Generating points distribution values and saving them to file...")
            self.load_distribution_parameter()

    def load_distribution_parameter(self):
        obj = distributionParameterPoints.DistributionParameterPoints()
        obj.calculate_distribution_parameter()
        obj.save_dist_parameter()
        self.dist_parameter_points = obj.dist_parameter_points

    def set_step_number(self, step_number):
        if step_number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            self.step_number = str(step_number)
        else:
            raise Exception("Step Number must be a value between 1 and 12.")

    def proactivity_encoding_to_text(self):
        if self.proactivity == [1, 0, 0, 0]:
            return 'none'
        elif self.proactivity == [0, 1, 0, 0]:
            return 'notification'
        elif self.proactivity == [0, 0, 1, 0]:
            return 'suggestion'
        elif self.proactivity == [0, 0, 0, 1]:
            return 'intervention'

    @staticmethod
    def helpsugg_request_to_code(sim_step_data):
        h = sim_step_data['helpRequest']
        s = sim_step_data['suggestionRequest']
        if h == 1 and s == 1:
            return 'Help1_Sugg1'
        elif h == 1 and s == 0:
            return 'Help1_Sugg0'
        elif h == 0 and s == 1:
            return 'Help0_Sugg1'
        elif h == 0 and s == 0:
            return 'Help0_Sugg0'

    def gen_points(self, pers_code, helpsugg):
        pro = self.proactivity_encoding_to_text()
        len_d = len(self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg])
        points = 0
        if len_d == 3:
            p_0 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_0']
            p_10 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_10']
            points = np.random.choice([0, 10], p=[p_0, p_10], size=1)[0]
        elif len_d == 4:
            p_0 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_0']
            p_10 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_10']
            p_20 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_20']
            points = np.random.choice([0, 10, 20], p=[p_0, p_10, p_20], size=1)[0]
        elif len_d == 5:
            p_0 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_0']
            p_10 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_10']
            p_20 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_20']
            p_30 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_30']
            points = np.random.choice([0, 10, 20, 30], p=[p_0, p_10, p_20, p_30], size=1)[0]
        elif len_d == 6:
            p_0 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_0']
            p_10 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_10']
            p_20 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_20']
            p_30 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_30']
            p_40 = self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['points_40']
            points = np.random.choice([0, 10, 20, 30, 40], p=[p_0, p_10, p_20, p_30, p_40], size=1)[0]

        self.simulated_step_data_points['points'] = points

    def generate_points(self, sim_step_data):
        if not self.step_number:
            raise Exception('You have to set step number.')

        self.simulated_step_data_points['step_number'] = int(self.step_number)
        self.simulated_step_data_points['proactivity'] = sim_step_data['proactivity']
        self.proactivity = sim_step_data['proactivity']
        helpsugg = self.helpsugg_request_to_code(sim_step_data=sim_step_data)
        pers_code = sim_step_data['pers_code']
        pro = self.proactivity_encoding_to_text()

        if self.dist_parameter_points[pers_code][pro][self.step_number]['overall']['#'] < 10:
            pers_code = 'overall'
        if self.dist_parameter_points[pers_code][pro][self.step_number][helpsugg]['#'] < 10:
            helpsugg = 'overall'

        self.simulated_step_data_points['used_values']['pers_code'] = pers_code
        self.simulated_step_data_points['used_values']['HelpSugg'] = helpsugg

        self.gen_points(pers_code=pers_code, helpsugg=helpsugg)


if __name__ == '__main__':
    o = GenPoints()
    for i in range(1, 13):
        o.set_step_number(i)
        o.generate_points(sim_step_data={'helpRequest': 0, 'suggestionRequest': 0,
                                         'proactivity': [0, 1, 0, 0], 'pers_code': '000'})
        print(o.simulated_step_data_points)
