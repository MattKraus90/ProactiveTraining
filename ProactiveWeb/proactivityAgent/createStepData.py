import json
import os

from proactivityAgent.distributionParameter import DistributionParameter
from proactivityAgent.utils import proactivity_encoding_to_text, read_json

DIRECTORY_PATH = os.path.dirname(__file__)

class StepData:
    def __init__(self):
        self.proactivity = None
        self.step_number = None
        self.help_req = None
        self.sugg_req = None
        self.duration = None
        self.difficulty = None
        
        self.__load_dist_params()
        self.__load_task_difficulties()
        
        self.step_data = {'helpRequest': 0, 'suggestionRequest': 0, 'duration': 0.0, 'difficulty': 0.0, 'proactivity': [],
                          'step_number': '', 'pers_code': '000', 'used_values': {'com': '', 'pers_c': '000', 'step_number': 0}}
            
    
    def __load_dist_params(self):
        try:
            file = open(os.path.join(DIRECTORY_PATH, 'data/dist_data.json'), 'r')
            self.dist_parameter = json.load(file)
            print('Loaded distribution parameter from file...')
        except FileNotFoundError:
            print('Generating distribution parameter and saving them to file...')
            obj = DistributionParameter()
            obj.main()
            self.dist_parameter = obj.dist_parameter
            
            
    def __load_task_difficulties(self):
        path = os.path.join(DIRECTORY_PATH, 'data/difficulties.json')
        self.task_difficulties = read_json(path)
        
        
    def __set_step_number(self, step_number):
        if step_number in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            self.step_number = step_number
        else:
            raise Exception(
                'Step number value has to be in the range of 1 to 12!')
    
    
    def __set_proactivity(self, proactivity):
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
    
    def __set_help_reqest(self, help_req):
        if help_req == 0 or help_req == 1:
            self.help_req = help_req
        else:
            raise Exception(
                'Help Request value must be 0 or 1'
                '0: Help not requested, 1: Help requested'
            )
    
    def __set_sugg_reqest(self, sugg_req):
        if sugg_req == 0 or sugg_req == 1:
            self.help_req = sugg_req
        else:
            raise Exception(
                'Suggestion Request value must be 0 or 1'
                '0: Help not requested, 1: Help requested'
            )
    
    def __set_duration(self, duration):
        if duration >= 20.0:
            self.duration = duration
        else:
            raise Exception(
                "Duration can't be under 20.0 seconds"
            )
    
    def __set_difficulty(self, step_number):
        if step_number in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            self.difficulty = self.task_difficulties[step_number]
        else:
            raise Exception(
                'Step number value has to be in the range of 1 to 12!')

    
    @staticmethod
    def __create_personality_code(pers_values):
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
    
    
    def set_step_data(self, step_number, proactivity, help_req, sugg_req, duration):
        self.__set_step_number(str(step_number))
        self.__set_proactivity(proactivity)
        self.__set_help_reqest(help_req)
        self.__set_sugg_reqest(sugg_req)
        self.__set_duration(duration)
        self.__set_difficulty(str(step_number))
    
    
    def get_step_data(self, pers_vals):
        pers_code = self.__create_personality_code(pers_vals)
        
        self.step_data['pers_code'] = pers_code
        self.step_data['proactivity'] = self.proactivity
        self.step_data['step_number'] = self.step_number
        self.step_data['helpRequest'] = self.help_req
        self.step_data['suggestionRequest'] = self.sugg_req
        self.step_data['duration'] = self.duration
        self.step_data['difficulty'] = self.difficulty
        
        pro = proactivity_encoding_to_text(self.proactivity)

        if self.dist_parameter[pers_code][pro]['0']['#'] < 10:
            pers_code = 'overall'
        if self.dist_parameter[pers_code][pro][self.step_number]['#'] < 10:
            pers_code = 'overall'
            
        self.step_data['used_values']['step_number'] = self.step_number
        self.step_data['used_values']['pers_c'] = pers_code
        