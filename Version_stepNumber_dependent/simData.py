# import pandas as pd
import numpy as np
from scipy import stats
import json
import distributionParameter


class SimData:

    def __init__(self):
        try:
            file = open('user_simulator_data/dist_data/dist_data.json', 'r')
            self.dist_parameter = json.load(file)
            print('Loaded distribution parameter from file...')
        except FileNotFoundError:
            print('Generating distribution parameter and saving them to file...')
            obj = distributionParameter.DistributionParameter()
            obj.main()
            self.dist_parameter = obj.dist_parameter

        self.dist_parameter_proact_none = {}
        self.dist_parameter_proact_notification = {}
        self.dist_parameter_proact_suggestion = {}
        self.dist_parameter_proact_intervention = {}

        self.proactivity = None
        self.step_number = None
        self.simulated_step_data = {'helpRequest': 0, 'suggestionRequest': 0, 'duration': 0.0, 'difficulty': 0.0,
                                    'proactivity': [], 'step_number': '', 'pers_code': '000',
                                    'used_values': {'com': '', 'pers_c': '000'}}

    def set_proactivity(self, proactivity):
        if proactivity in [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]:
            self.proactivity = proactivity
            # [1, 0, 0, 0] = None
            # [0, 1, 0, 0] = Notification
            # [0, 0, 1, 0] = Suggestion
            # [0, 0, 0, 1] = Intervention
        else:
            raise Exception(
                'Proactivity-value must be one of these: [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] '
                '(None, Notification, Suggestion, Intervention)')

    def set_step_number(self, step_number):
        if step_number in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            self.step_number = step_number
        else:
            raise Exception(
                'Step number value has to be in the range of 1 to 12!')

    def gen_help_request(self):
        prob_true = 0
        if self.proactivity == [1, 0, 0, 0]:
            prob_true = self.dist_parameter_proact_none[self.step_number]['HelpRequest']
        elif self.proactivity == [0, 1, 0, 0]:
            prob_true = self.dist_parameter_proact_notification[self.step_number]['HelpRequest']
        elif self.proactivity == [0, 0, 1, 0]:
            prob_true = self.dist_parameter_proact_suggestion[self.step_number]['HelpRequest']
        elif self.proactivity == [0, 0, 0, 1]:
            prob_true = self.dist_parameter_proact_intervention[self.step_number]['HelpRequest']
        prob_false = 1 - prob_true

        self.simulated_step_data['helpRequest'] = int(np.random.choice([0, 1], p=[prob_false, prob_true], size=1))

    def gen_sugg_request(self):
        prob_true = 0
        if self.proactivity == [1, 0, 0, 0]:
            prob_true = self.dist_parameter_proact_none[self.step_number]['SuggRequest']
        elif self.proactivity == [0, 1, 0, 0]:
            prob_true = self.dist_parameter_proact_notification[self.step_number]['SuggRequest']
        elif self.proactivity == [0, 0, 1, 0]:
            prob_true = self.dist_parameter_proact_suggestion[self.step_number]['SuggRequest']
        elif self.proactivity == [0, 0, 0, 1]:
            prob_true = self.dist_parameter_proact_intervention[self.step_number]['SuggRequest']
        prob_false = 1 - prob_true

        self.simulated_step_data['suggestionRequest'] = int(np.random.choice([0, 1], p=[prob_false, prob_true], size=1))

    def gen_duration(self):
        mean = 0
        std = 0
        # help_req = self.simulated_step_data['helpRequest']
        # sugg_req = self.simulated_step_data['suggestionRequest']
        lower = 20
        help_req = 0
        sugg_req = 0
        if self.proactivity == [1, 0, 0, 0]:
            mean = self.dist_parameter_proact_none[self.step_number]['Duration']['overall']['mean']
            std = self.dist_parameter_proact_none[self.step_number]['Duration']['overall']['std']
            if help_req == 1 and sugg_req == 1:
                if self.dist_parameter_proact_none[self.step_number]['Duration']['Help1_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_none[self.step_number]['Duration']['Help1_Sugg1']['mean']
                    std = self.dist_parameter_proact_none[self.step_number]['Duration']['Help1_Sugg1']['std']
            elif help_req == 1 and sugg_req == 0:
                if self.dist_parameter_proact_none[self.step_number]['Duration']['Help1_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_none[self.step_number]['Duration']['Help1_Sugg0']['mean']
                    std = self.dist_parameter_proact_none[self.step_number]['Duration']['Help1_Sugg0']['std']
            elif help_req == 0 and sugg_req == 1:
                if self.dist_parameter_proact_none[self.step_number]['Duration']['Help0_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_none[self.step_number]['Duration']['Help0_Sugg1']['mean']
                    std = self.dist_parameter_proact_none[self.step_number]['Duration']['Help0_Sugg1']['std']
            elif help_req == 0 and sugg_req == 0:
                if self.dist_parameter_proact_none[self.step_number]['Duration']['Help0_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_none[self.step_number]['Duration']['Help0_Sugg0']['mean']
                    std = self.dist_parameter_proact_none[self.step_number]['Duration']['Help0_Sugg0']['std']
        elif self.proactivity == [0, 1, 0, 0]:
            mean = self.dist_parameter_proact_notification[self.step_number]['Duration']['overall']['mean']
            std = self.dist_parameter_proact_notification[self.step_number]['Duration']['overall']['std']
            if help_req == 1 and sugg_req == 1:
                if self.dist_parameter_proact_notification[self.step_number]['Duration']['Help1_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_notification[self.step_number]['Duration']['Help1_Sugg1']['mean']
                    std = self.dist_parameter_proact_notification[self.step_number]['Duration']['Help1_Sugg1']['std']
            elif help_req == 1 and sugg_req == 0:
                if self.dist_parameter_proact_notification[self.step_number]['Duration']['Help1_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_notification[self.step_number]['Duration']['Help1_Sugg0']['mean']
                    std = self.dist_parameter_proact_notification[self.step_number]['Duration']['Help1_Sugg0']['std']
            elif help_req == 0 and sugg_req == 1:
                if self.dist_parameter_proact_notification[self.step_number]['Duration']['Help0_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_notification[self.step_number]['Duration']['Help0_Sugg1']['mean']
                    std = self.dist_parameter_proact_notification[self.step_number]['Duration']['Help0_Sugg1']['std']
            elif help_req == 0 and sugg_req == 0:
                if self.dist_parameter_proact_notification[self.step_number]['Duration']['Help0_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_notification[self.step_number]['Duration']['Help0_Sugg0']['mean']
                    std = self.dist_parameter_proact_notification[self.step_number]['Duration']['Help0_Sugg0']['std']
        elif self.proactivity == [0, 0, 1, 0]:
            mean = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['overall']['mean']
            std = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['overall']['std']
            if help_req == 1 and sugg_req == 1:
                if self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help1_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help1_Sugg1']['mean']
                    std = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help1_Sugg1']['std']
            elif help_req == 1 and sugg_req == 0:
                if self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help1_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help1_Sugg0']['mean']
                    std = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help1_Sugg0']['std']
            elif help_req == 0 and sugg_req == 1:
                if self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help0_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help0_Sugg1']['mean']
                    std = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help0_Sugg1']['std']
            elif help_req == 0 and sugg_req == 0:
                if self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help0_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help0_Sugg0']['mean']
                    std = self.dist_parameter_proact_suggestion[self.step_number]['Duration']['Help0_Sugg0']['std']
        elif self.proactivity == [0, 0, 0, 1]:
            mean = self.dist_parameter_proact_intervention[self.step_number]['Duration']['overall']['mean']
            std = self.dist_parameter_proact_intervention[self.step_number]['Duration']['overall']['std']
            if help_req == 1 and sugg_req == 1:
                if self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help1_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help1_Sugg1']['mean']
                    std = self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help1_Sugg1']['std']
            elif help_req == 1 and sugg_req == 0:
                if self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help1_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help1_Sugg0']['mean']
                    std = self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help1_Sugg0']['std']
            elif help_req == 0 and sugg_req == 1:
                if self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help0_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help0_Sugg1']['mean']
                    std = self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help0_Sugg1']['std']
            elif help_req == 0 and sugg_req == 0:
                if self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help0_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help0_Sugg0']['mean']
                    std = self.dist_parameter_proact_intervention[self.step_number]['Duration']['Help0_Sugg0']['std']

        # self.simulated_step_data['duration'] = float(
        #     np.around(np.random.normal(loc=mean, scale=std, size=1), decimals=0))
        if std == 0.0:
            self.simulated_step_data['duration'] = mean
        else:
            truncated_norm_dist = stats.truncnorm(a=((lower - mean) / std), b=np.inf, loc=mean, scale=std)
            self.simulated_step_data['duration'] = float(
                np.around(truncated_norm_dist.rvs(1), decimals=0))

    def gen_difficulty(self):
        mean = 0
        std = 0
        lower, upper = 1, 5
        help_req = self.simulated_step_data['helpRequest']
        sugg_req = self.simulated_step_data['suggestionRequest']
        if self.proactivity == [1, 0, 0, 0]:
            mean = self.dist_parameter_proact_none[self.step_number]['Difficulty']['overall']['mean']
            std = self.dist_parameter_proact_none[self.step_number]['Difficulty']['overall']['std']
            if help_req == 1 and sugg_req == 1:
                if self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help1_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help1_Sugg1']['mean']
                    std = self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help1_Sugg1']['std']
            elif help_req == 1 and sugg_req == 0:
                if self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help1_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help1_Sugg0']['mean']
                    std = self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help1_Sugg0']['std']
            elif help_req == 0 and sugg_req == 1:
                if self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help0_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help0_Sugg1']['mean']
                    std = self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help0_Sugg1']['std']
            elif help_req == 0 and sugg_req == 0:
                if self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help0_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help0_Sugg0']['mean']
                    std = self.dist_parameter_proact_none[self.step_number]['Difficulty']['Help0_Sugg0']['std']
        elif self.proactivity == [0, 1, 0, 0]:
            mean = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['overall']['mean']
            std = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['overall']['std']
            if help_req == 1 and sugg_req == 1:
                if self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help1_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help1_Sugg1'][
                        'mean']
                    std = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help1_Sugg1']['std']
            elif help_req == 1 and sugg_req == 0:
                if self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help1_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help1_Sugg0'][
                        'mean']
                    std = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help1_Sugg0']['std']
            elif help_req == 0 and sugg_req == 1:
                if self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help0_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help0_Sugg1'][
                        'mean']
                    std = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help0_Sugg1']['std']
            elif help_req == 0 and sugg_req == 0:
                if self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help0_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help0_Sugg0'][
                        'mean']
                    std = self.dist_parameter_proact_notification[self.step_number]['Difficulty']['Help0_Sugg0']['std']
        elif self.proactivity == [0, 0, 1, 0]:
            mean = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['overall']['mean']
            std = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['overall']['std']
            if help_req == 1 and sugg_req == 1:
                if self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help1_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help1_Sugg1']['mean']
                    std = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help1_Sugg1']['std']
            elif help_req == 1 and sugg_req == 0:
                if self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help1_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help1_Sugg0']['mean']
                    std = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help1_Sugg0']['std']
            elif help_req == 0 and sugg_req == 1:
                if self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help0_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help0_Sugg1']['mean']
                    std = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help0_Sugg1']['std']
            elif help_req == 0 and sugg_req == 0:
                if self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help0_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help0_Sugg0']['mean']
                    std = self.dist_parameter_proact_suggestion[self.step_number]['Difficulty']['Help0_Sugg0']['std']
        elif self.proactivity == [0, 0, 0, 1]:
            mean = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['overall']['mean']
            std = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['overall']['std']
            if help_req == 1 and sugg_req == 1:
                if self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help1_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help1_Sugg1'][
                        'mean']
                    std = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help1_Sugg1']['std']
            elif help_req == 1 and sugg_req == 0:
                if self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help1_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help1_Sugg0'][
                        'mean']
                    std = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help1_Sugg0']['std']
            elif help_req == 0 and sugg_req == 1:
                if self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help0_Sugg1']['#'] > 10:
                    mean = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help0_Sugg1'][
                        'mean']
                    std = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help0_Sugg1']['std']
            elif help_req == 0 and sugg_req == 0:
                if self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help0_Sugg0']['#'] > 10:
                    mean = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help0_Sugg0'][
                        'mean']
                    std = self.dist_parameter_proact_intervention[self.step_number]['Difficulty']['Help0_Sugg0']['std']
        # self.simulated_step_data['difficulty'] = float(
        #     np.around(np.random.normal(loc=mean, scale=std, size=1), decimals=0))
        if std == 0.0:
            self.simulated_step_data['difficulty'] = mean
        else:
            truncated_norm_dist = stats.truncnorm(
                (lower - mean) / std, (upper - mean) / std, loc=mean, scale=std)
            self.simulated_step_data['difficulty'] = float(
                np.around(truncated_norm_dist.rvs(1), decimals=0))

    @staticmethod
    def create_personality_code(pers_values):
        man_exp = pers_values['management experience']
        pre_trust = pers_values['preTrust']
        tech_aff = pers_values['technical affinity']
        code = ''

        if man_exp <= 3.0:
            code += '0'
        else:
            code += '1'
        if pre_trust <= 3.0:
            code += '0'
        else:
            code += '1'
        if tech_aff <= 3.0:
            code += '0'
        else:
            code += '1'

        return code

    def proactivity_encoding_to_text(self):
        if self.proactivity == [1, 0, 0, 0]:
            return 'none'
        elif self.proactivity == [0, 1, 0, 0]:
            return 'notification'
        elif self.proactivity == [0, 0, 1, 0]:
            return 'suggestion'
        elif self.proactivity == [0, 0, 0, 1]:
            return 'intervention'

    def generate_values(self, personality_values):
        if not self.proactivity:
            raise Exception('You have to set proactivity.')
        if not self.step_number:
            raise Exception('You have to set Complexity.')

        self.simulated_step_data['proactivity'] = self.proactivity
        self.simulated_step_data['step_number'] = self.step_number

        pers_code = self.create_personality_code(personality_values)
        self.simulated_step_data['pers_code'] = pers_code

        pro = self.proactivity_encoding_to_text()

        if self.dist_parameter[pers_code][pro]['0']['#'] < 10:
            pers_code = 'overall'
        if self.dist_parameter[pers_code][pro][self.step_number]['#'] < 10:
            # self.step_number = '0'
            pers_code = 'overall'

        self.simulated_step_data['used_values']['step_number'] = self.step_number
        self.simulated_step_data['used_values']['pers_c'] = pers_code

        self.dist_parameter_proact_none = self.dist_parameter[pers_code]['none']
        self.dist_parameter_proact_notification = self.dist_parameter[pers_code]['notification']
        self.dist_parameter_proact_suggestion = self.dist_parameter[pers_code]['suggestion']
        self.dist_parameter_proact_intervention = self.dist_parameter[pers_code]['intervention']

        self.gen_help_request()
        self.gen_sugg_request()
        self.gen_duration()
        self.gen_difficulty()


if __name__ == '__main__':
    sD = SimData()
    sD.set_proactivity([0, 0, 0, 1])
    sD.set_step_number('5')
    sD.generate_values({'technical affinity': 4.0, 'management experience': 0.0, 'preTrust': 0.0})
    print(sD.simulated_step_data)
    # saver = dataSaver.DataSaver()
    # saver.save_dist_data_to_json({'none': sD.dist_parameter_proact_none,
    #                              'notification': sD.dist_parameter_proact_notification,
    #                              'suggestion': sD.dist_parameter_proact_suggestion,
    #                              'intervention': sD.dist_parameter_proact_intervention})
