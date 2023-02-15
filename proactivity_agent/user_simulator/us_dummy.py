import numpy as np


class DummyClass:
    def __init__(self):
        self.action = 0
        self.relevant_data = {'trust': 1, 'points': 0}

    def generate_person_data(self):
        pass

    def simulate(self, step_number, action):
        self.relevant_data['trust'] = np.random.choice([1, 2, 3, 4, 5])
        self.relevant_data['points'] = np.random.choice([0, 20, 30, 40])
        return np.array([self.relevant_data['trust']]).astype(np.float32)
