import numpy as np


class PersonalDetails:
    """
    PersonalDetails class represents personal details of a user

    Attributes:
        pers_data (dict): Dictionary containing the user's personal data
    """

    def __init__(self):
        # Initializes an instance of the PersonalDetails class with an empty dictionary for storing personal data
        self.pers_data = {'age': 0.0, 'gender': '', 'technical affinity': 0.0, 'management experience': 0.0,
                          'preTrust': 0.0, 'neuroticism': 0.0, 'extraversion': 0.0, 'openness': 0.0,
                          'agreeableness': 0.0, 'conscientiousness': 0.0}

    def __get_age(self):
        # Retrieves and sets the user's age
        self.pers_data['age'] = np.float64(self.pers_data_dict['age'])

    def __get_gender(self):
        # Retrieves and sets the user's gender
        self.pers_data['gender'] = self.pers_data_dict['gender']

    def __get_technaff(self):
        # Retrieves and sets the user's technical affinity
        technaff = np.array([self.pers_data_dict['TA1'], self.pers_data_dict['TA2'], self.pers_data_dict['TA3'],
                             self.pers_data_dict['TA4'], self.__convert_val(
                                 self.pers_data_dict['TA5']),
                             self.__convert_val(self.pers_data_dict['TA6'])], dtype=np.float64)

        technaff = np.mean(technaff)
        self.pers_data['technical affinity'] = float(
            np.around(technaff, decimals=0))

    def __get_managexp(self):
        # Retrieves and sets the user's management experience
        managexp = np.array([self.pers_data_dict['ExperienceEco1'], self.pers_data_dict['ExperienceEco2'],
                             self.pers_data_dict['ExperienceEco3']], dtype=np.float64)

        managexp = np.mean(managexp)
        self.pers_data['management experience'] = float(
            np.around(managexp, decimals=0))

    def __get_pretrust(self):
        # Retrieves and sets the user's pre-trust value
        pretrust = np.array([self.pers_data_dict['PreTrust1'], self.__convert_val(self.pers_data_dict['PreTrust2']),
                             self.pers_data_dict['PreTrust3'], self.pers_data_dict['PreTrust4'],
                             self.pers_data_dict['PreTrust5'], self.pers_data_dict['PreTrust6']], dtype=np.float64)

        pretrust = np.mean(pretrust)
        self.pers_data['preTrust'] = float(np.around(pretrust, decimals=0))

    def __get_neuroticism(self):
        # Retrieves and sets the user's neuroticism value
        neuroticism = np.array([self.__convert_val(self.pers_data_dict['Personality4']),
                                self.pers_data_dict['Personality8']], dtype=np.float64)

        neuroticism = np.mean(neuroticism)
        self.pers_data['neuroticism'] = float(
            np.around(neuroticism, decimals=0))

    def __get_extraversion(self):
        # Retrieves and sets the user's extraversion value
        extraversion = np.array([self.__convert_val(self.pers_data_dict['Personality1']),
                                 self.pers_data_dict['Personality6']], dtype=np.float64)

        extraversion = np.mean(extraversion)
        self.pers_data['extraversion'] = float(
            np.around(extraversion, decimals=0))

    def __get_openness(self):
        # Retrieves and sets the user's openness value
        openness = np.array([self.__convert_val(self.pers_data_dict['Personality5']),
                             self.pers_data_dict['Personality10']], dtype=np.float64)

        openness = np.mean(openness)
        self.pers_data['openness'] = float(np.around(openness, decimals=0))

    def __get_agreeableness(self):
        # Retrieves and sets the user's agreeableness value
        agreeableness = np.array([self.pers_data_dict['Personality2'], self.__convert_val(self.pers_data_dict['Personality9'])],
                                 dtype=np.float64)

        agreeableness = np.mean(agreeableness)
        self.pers_data['agreeableness'] = float(
            np.around(agreeableness, decimals=0))

    def __get_conscientiousness(self):
        # Retrieves and sets the user's conscientiousness value
        conscientiousness = np.array([self.__convert_val(self.pers_data_dict['Personality3']), self.pers_data_dict['Personality7']],
                                     dtype=np.float64)

        conscientiousness = np.mean(conscientiousness)
        self.pers_data['conscientiousness'] = float(
            np.around(conscientiousness, decimals=0))

    def __convert_val(self, val):
        # Converts a value to its corresponding value
        if val == '1':
            return '5'
        elif val == '2':
            return '4'
        elif val == '4':
            return '2'
        elif val == '5':
            return '1'
        else:
            return val

    def generate_person_data(self, pers_data_dict):
        # Generates the user's personal data based on the given dictionary
        self.pers_data_dict = pers_data_dict

        self.__get_age()
        self.__get_gender()
        self.__get_technaff()
        self.__get_managexp()
        self.__get_pretrust()
        self.__get_neuroticism()
        self.__get_extraversion()
        self.__get_openness()
        self.__get_agreeableness()
        self.__get_conscientiousness()

        return self.pers_data
