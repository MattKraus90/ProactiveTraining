import json
import os
from copy import deepcopy

import numpy as np
import pandas as pd
from proactivityAgent.datasets import GenDatasets
from proactivityAgent.distribution_parameter_dict import \
    DistParameterDataStructures


class DistributionParameter:
    def __init__(self):
        self.dataset_obj = GenDatasets()
        distribution_parameter_obj = DistParameterDataStructures()
        self.dist_parameter = distribution_parameter_obj.dist_parameter

        self.df_proact_none = pd.DataFrame()
        self.df_proact_notification = pd.DataFrame()
        self.df_proact_suggestion = pd.DataFrame()
        self.df_proact_intervention = pd.DataFrame()

        """paramter for different normal distribution, sorted after proactivity and complexity
            complexity: 0 -> calculated parameters over the whole dataset
                        3 -> calculated parameters over step-data with complexity 3 (1, 4, 7, 10)
                        4 -> calculated parameters over step-data with complexity 4 (2, 5, 8, 11)
                        5 -> calculated parameters over step-data with complexity 5 (3, 6, 9, 12)"""
        self.dist_parameter_proact_none = {'0': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '1': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '2': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '3': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '4': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '5': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '6': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '7': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '8': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '9': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                 'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                 'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                'overall': {'mean': 0.0, 'std': 0.0}},
                                                 '#': 0
                                                 },
                                           '10': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                  'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'overall': {'mean': 0.0, 'std': 0.0}},
                                                  'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'overall': {'mean': 0.0, 'std': 0.0}},
                                                  '#': 0
                                                  },
                                           '11': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                  'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'overall': {'mean': 0.0, 'std': 0.0}},
                                                  'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'overall': {'mean': 0.0, 'std': 0.0}},
                                                  '#': 0
                                                  },
                                           '12': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                  'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                               'overall': {'mean': 0.0, 'std': 0.0}},
                                                  'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                 'overall': {'mean': 0.0, 'std': 0.0}},
                                                  '#': 0
                                                  }
                                           }

        self.dist_parameter_proact_notification = {'0': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '1': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '2': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '3': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '4': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '5': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '6': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '7': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '8': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '9': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '10': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                          'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                          'Difficulty': {
                                                              'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                          '#': 0
                                                          },
                                                   '11': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                          'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                          'Difficulty': {
                                                              'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                          '#': 0
                                                          },
                                                   '12': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                          'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                          'Difficulty': {
                                                              'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                          '#': 0
                                                          }
                                                   }

        self.dist_parameter_proact_suggestion = {'0': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '1': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '2': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '3': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '4': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '5': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '6': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '7': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '8': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '9': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                       'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                    'overall': {'mean': 0.0, 'std': 0.0}},
                                                       'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                       '#': 0
                                                       },
                                                 '10': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                        'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'overall': {'mean': 0.0, 'std': 0.0}},
                                                        'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                        '#': 0
                                                        },
                                                 '11': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                        'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'overall': {'mean': 0.0, 'std': 0.0}},
                                                        'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                        '#': 0
                                                        },
                                                 '12': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                        'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                     'overall': {'mean': 0.0, 'std': 0.0}},
                                                        'Difficulty': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                        '#': 0
                                                        }
                                                 }

        self.dist_parameter_proact_intervention = {'0': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '1': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '2': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '3': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '4': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '5': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '6': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '7': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '8': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '9': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                         'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                      'overall': {'mean': 0.0, 'std': 0.0}},
                                                         'Difficulty': {
                                                             'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                             'overall': {'mean': 0.0, 'std': 0.0}},
                                                         '#': 0
                                                         },
                                                   '10': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                          'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                          'Difficulty': {
                                                              'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                          '#': 0
                                                          },
                                                   '11': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                          'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                          'Difficulty': {
                                                              'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                          '#': 0
                                                          },
                                                   '12': {'HelpRequest': 0.0, 'SuggRequest': 0.0,
                                                          'Duration': {'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                                       'overall': {'mean': 0.0, 'std': 0.0}},
                                                          'Difficulty': {
                                                              'Help1_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help1_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg1': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'Help0_Sugg0': {'mean': 0.0, 'std': 0.0, '#': 0},
                                                              'overall': {'mean': 0.0, 'std': 0.0}},
                                                          '#': 0
                                                          }
                                                   }

    def load_datasets(self, personality_values):

        self.df_proact_none = self.dataset_obj.df_dict[personality_values]['none']
        self.df_proact_notification = self.dataset_obj.df_dict[personality_values]['notification']
        self.df_proact_suggestion = self.dataset_obj.df_dict[personality_values]['suggestion']
        self.df_proact_intervention = self.dataset_obj.df_dict[personality_values]['intervention']

    def save_dataset_lengths(self):
        self.dist_parameter_proact_none['0']['#'] = len(
            self.df_proact_none['0'].index)
        self.dist_parameter_proact_notification['0']['#'] = len(
            self.df_proact_notification['0'].index)
        self.dist_parameter_proact_suggestion['0']['#'] = len(
            self.df_proact_suggestion['0'].index)
        self.dist_parameter_proact_intervention['0']['#'] = len(
            self.df_proact_intervention['0'].index)

        self.dist_parameter_proact_none['1']['#'] = len(
            self.df_proact_none['1'].index)
        self.dist_parameter_proact_none['2']['#'] = len(
            self.df_proact_none['2'].index)
        self.dist_parameter_proact_none['3']['#'] = len(
            self.df_proact_none['3'].index)
        self.dist_parameter_proact_none['4']['#'] = len(
            self.df_proact_none['4'].index)
        self.dist_parameter_proact_none['5']['#'] = len(
            self.df_proact_none['5'].index)
        self.dist_parameter_proact_none['6']['#'] = len(
            self.df_proact_none['6'].index)
        self.dist_parameter_proact_none['7']['#'] = len(
            self.df_proact_none['7'].index)
        self.dist_parameter_proact_none['8']['#'] = len(
            self.df_proact_none['8'].index)
        self.dist_parameter_proact_none['9']['#'] = len(
            self.df_proact_none['9'].index)
        self.dist_parameter_proact_none['10']['#'] = len(
            self.df_proact_none['10'].index)
        self.dist_parameter_proact_none['11']['#'] = len(
            self.df_proact_none['11'].index)
        self.dist_parameter_proact_none['12']['#'] = len(
            self.df_proact_none['12'].index)

        self.dist_parameter_proact_notification['1']['#'] = len(
            self.df_proact_notification['1'].index)
        self.dist_parameter_proact_notification['2']['#'] = len(
            self.df_proact_notification['2'].index)
        self.dist_parameter_proact_notification['3']['#'] = len(
            self.df_proact_notification['3'].index)
        self.dist_parameter_proact_notification['4']['#'] = len(
            self.df_proact_notification['4'].index)
        self.dist_parameter_proact_notification['5']['#'] = len(
            self.df_proact_notification['5'].index)
        self.dist_parameter_proact_notification['6']['#'] = len(
            self.df_proact_notification['6'].index)
        self.dist_parameter_proact_notification['7']['#'] = len(
            self.df_proact_notification['7'].index)
        self.dist_parameter_proact_notification['8']['#'] = len(
            self.df_proact_notification['8'].index)
        self.dist_parameter_proact_notification['9']['#'] = len(
            self.df_proact_notification['9'].index)
        self.dist_parameter_proact_notification['10']['#'] = len(
            self.df_proact_notification['10'].index)
        self.dist_parameter_proact_notification['11']['#'] = len(
            self.df_proact_notification['11'].index)
        self.dist_parameter_proact_notification['12']['#'] = len(
            self.df_proact_notification['12'].index)

        self.dist_parameter_proact_suggestion['1']['#'] = len(
            self.df_proact_suggestion['1'].index)
        self.dist_parameter_proact_suggestion['2']['#'] = len(
            self.df_proact_suggestion['2'].index)
        self.dist_parameter_proact_suggestion['3']['#'] = len(
            self.df_proact_suggestion['3'].index)
        self.dist_parameter_proact_suggestion['4']['#'] = len(
            self.df_proact_suggestion['4'].index)
        self.dist_parameter_proact_suggestion['5']['#'] = len(
            self.df_proact_suggestion['5'].index)
        self.dist_parameter_proact_suggestion['6']['#'] = len(
            self.df_proact_suggestion['6'].index)
        self.dist_parameter_proact_suggestion['7']['#'] = len(
            self.df_proact_suggestion['7'].index)
        self.dist_parameter_proact_suggestion['8']['#'] = len(
            self.df_proact_suggestion['8'].index)
        self.dist_parameter_proact_suggestion['9']['#'] = len(
            self.df_proact_suggestion['9'].index)
        self.dist_parameter_proact_suggestion['10']['#'] = len(
            self.df_proact_suggestion['10'].index)
        self.dist_parameter_proact_suggestion['11']['#'] = len(
            self.df_proact_suggestion['11'].index)
        self.dist_parameter_proact_suggestion['12']['#'] = len(
            self.df_proact_suggestion['12'].index)

        self.dist_parameter_proact_intervention['1']['#'] = len(
            self.df_proact_intervention['1'].index)
        self.dist_parameter_proact_intervention['2']['#'] = len(
            self.df_proact_intervention['2'].index)
        self.dist_parameter_proact_intervention['3']['#'] = len(
            self.df_proact_intervention['3'].index)
        self.dist_parameter_proact_intervention['4']['#'] = len(
            self.df_proact_intervention['4'].index)
        self.dist_parameter_proact_intervention['5']['#'] = len(
            self.df_proact_intervention['5'].index)
        self.dist_parameter_proact_intervention['6']['#'] = len(
            self.df_proact_intervention['6'].index)
        self.dist_parameter_proact_intervention['7']['#'] = len(
            self.df_proact_intervention['7'].index)
        self.dist_parameter_proact_intervention['8']['#'] = len(
            self.df_proact_intervention['8'].index)
        self.dist_parameter_proact_intervention['9']['#'] = len(
            self.df_proact_intervention['9'].index)
        self.dist_parameter_proact_intervention['10']['#'] = len(
            self.df_proact_intervention['10'].index)
        self.dist_parameter_proact_intervention['11']['#'] = len(
            self.df_proact_intervention['11'].index)
        self.dist_parameter_proact_intervention['12']['#'] = len(
            self.df_proact_intervention['12'].index)

    def load_distribution_parameter_overall(self, step_number):
        """Calculates distribution values for Duration, Difficulty, HelpRequest, SuggestionRequest.
        the parameter for duration and difficulty are independent from Help- and SuggestionRequest"""
        # print(self.df['ProactiveTask1'].value_counts())

        self.dist_parameter_proact_none[step_number]['Duration']['overall']['mean'] = float(
            np.mean(self.df_proact_none[step_number]['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Duration']['overall']['std'] = float(
            np.std(self.df_proact_none[step_number]['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['overall']['mean'] = float(
            np.mean(self.df_proact_none[step_number]['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['overall']['std'] = float(
            np.std(self.df_proact_none[step_number]['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['HelpRequest'] = float(
            np.mean(self.df_proact_none[step_number]['HelpTask']))
        self.dist_parameter_proact_none[step_number]['SuggRequest'] = float(
            np.mean(self.df_proact_none[step_number]['SuggTask']))

        self.dist_parameter_proact_notification[step_number]['Duration']['overall']['mean'] = float(
            np.mean(self.df_proact_notification[step_number]['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Duration']['overall']['std'] = float(
            np.std(self.df_proact_notification[step_number]['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['overall']['mean'] = float(
            np.mean(self.df_proact_notification[step_number]['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['overall']['std'] = float(
            np.std(self.df_proact_notification[step_number]['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['HelpRequest'] = float(
            np.mean(self.df_proact_notification[step_number]['HelpTask']))
        self.dist_parameter_proact_notification[step_number]['SuggRequest'] = float(
            np.mean(self.df_proact_notification[step_number]['SuggTask']))

        self.dist_parameter_proact_suggestion[step_number]['Duration']['overall']['mean'] = float(
            np.mean(self.df_proact_suggestion[step_number]['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Duration']['overall']['std'] = float(
            np.std(self.df_proact_suggestion[step_number]['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['overall']['mean'] = float(
            np.mean(self.df_proact_suggestion[step_number]['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['overall']['std'] = float(
            np.std(self.df_proact_suggestion[step_number]['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['HelpRequest'] = float(
            np.mean(self.df_proact_suggestion[step_number]['HelpTask']))
        self.dist_parameter_proact_suggestion[step_number]['SuggRequest'] = float(
            np.mean(self.df_proact_suggestion[step_number]['SuggTask']))

        self.dist_parameter_proact_intervention[step_number]['Duration']['overall']['mean'] = float(
            np.mean(self.df_proact_intervention[step_number]['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Duration']['overall']['std'] = float(
            np.std(self.df_proact_intervention[step_number]['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['overall']['mean'] = float(
            np.mean(self.df_proact_intervention[step_number]['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['overall']['std'] = float(
            np.std(self.df_proact_intervention[step_number]['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['HelpRequest'] = float(
            np.mean(self.df_proact_intervention[step_number]['HelpTask']))
        self.dist_parameter_proact_intervention[step_number]['SuggRequest'] = float(
            np.mean(self.df_proact_intervention[step_number]['SuggTask']))

    def load_distribution_parameter_correlated(self, step_number):
        """Calculates distribution values for Duration, Difficulty, HelpRequest, SuggestionRequest.
                the parameter for duration and difficulty are dependent from Help- and SuggestionRequest"""
        # print(self.df['SuggTask'].value_counts())
        # print(self.df['HelpTask'].value_counts())

        # print(self.df_proact_none[step_number]['HelpTask'].value_counts())

        df_none_h1 = self.df_proact_none[step_number][self.df_proact_none[step_number]['HelpTask'] == 1]
        df_none_h0 = self.df_proact_none[step_number][self.df_proact_none[step_number]['HelpTask'] == 0]
        df_none_h1s1 = df_none_h1[df_none_h1['SuggTask'] == 1]
        df_none_h1s0 = df_none_h1[df_none_h1['SuggTask'] == 0]
        df_none_h0s1 = df_none_h0[df_none_h0['SuggTask'] == 1]
        df_none_h0s0 = df_none_h0[df_none_h0['SuggTask'] == 0]

        # df_none_h1s1.to_csv('Test/df_h1s1.csv', sep=',')
        # df_none_h1s0.to_csv('Test/df_h1s0.csv', sep=',')
        # df_none_h0s1.to_csv('Test/df_h0s1.csv', sep=',')
        # df_none_h0s0.to_csv('Test/df_h0s0.csv', sep=',')

        self.dist_parameter_proact_none[step_number]['Duration']['Help1_Sugg1']['#'] = len(
            df_none_h1s1.index)
        self.dist_parameter_proact_none[step_number]['Duration']['Help1_Sugg0']['#'] = len(
            df_none_h1s0.index)
        self.dist_parameter_proact_none[step_number]['Duration']['Help0_Sugg1']['#'] = len(
            df_none_h0s1.index)
        self.dist_parameter_proact_none[step_number]['Duration']['Help0_Sugg0']['#'] = len(
            df_none_h0s0.index)
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help1_Sugg1']['#'] = len(
            df_none_h1s1.index)
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help1_Sugg0']['#'] = len(
            df_none_h1s0.index)
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help0_Sugg1']['#'] = len(
            df_none_h0s1.index)
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help0_Sugg0']['#'] = len(
            df_none_h0s0.index)

        self.dist_parameter_proact_none[step_number]['Duration']['Help1_Sugg1']['mean'] = float(
            np.mean(df_none_h1s1['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Duration']['Help1_Sugg1']['std'] = float(
            np.std(df_none_h1s1['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Duration']['Help1_Sugg0']['mean'] = float(
            np.mean(df_none_h1s0['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Duration']['Help1_Sugg0']['std'] = float(
            np.std(df_none_h1s0['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Duration']['Help0_Sugg1']['mean'] = float(
            np.mean(df_none_h0s1['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Duration']['Help0_Sugg1']['std'] = float(
            np.std(df_none_h0s1['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Duration']['Help0_Sugg0']['mean'] = float(
            np.mean(df_none_h0s0['TimeDurationTask']))
        self.dist_parameter_proact_none[step_number]['Duration']['Help0_Sugg0']['std'] = float(
            np.std(df_none_h0s0['TimeDurationTask']))

        self.dist_parameter_proact_none[step_number]['Difficulty']['Help1_Sugg1']['mean'] = float(
            np.mean(df_none_h1s1['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help1_Sugg1']['std'] = float(
            np.std(df_none_h1s1['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help1_Sugg0']['mean'] = float(
            np.mean(df_none_h1s0['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help1_Sugg0']['std'] = float(
            np.std(df_none_h1s0['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help0_Sugg1']['mean'] = float(
            np.mean(df_none_h0s1['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help0_Sugg1']['std'] = float(
            np.std(df_none_h0s1['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help0_Sugg0']['mean'] = float(
            np.mean(df_none_h0s0['difficultyTask']))
        self.dist_parameter_proact_none[step_number]['Difficulty']['Help0_Sugg0']['std'] = float(
            np.std(df_none_h0s0['difficultyTask']))

        df_notification_h1 = self.df_proact_notification[step_number][
            self.df_proact_notification[step_number]['HelpTask'] == 1]
        df_notification_h0 = self.df_proact_notification[step_number][
            self.df_proact_notification[step_number]['HelpTask'] == 0]
        df_notification_h1s1 = df_notification_h1[df_notification_h1['SuggTask'] == 1]
        df_notification_h1s0 = df_notification_h1[df_notification_h1['SuggTask'] == 0]
        df_notification_h0s1 = df_notification_h0[df_notification_h0['SuggTask'] == 1]
        df_notification_h0s0 = df_notification_h0[df_notification_h0['SuggTask'] == 0]

        self.dist_parameter_proact_notification[step_number]['Duration']['Help1_Sugg1']['#'] = len(
            df_notification_h1s1.index)
        self.dist_parameter_proact_notification[step_number]['Duration']['Help1_Sugg0']['#'] = len(
            df_notification_h1s0.index)
        self.dist_parameter_proact_notification[step_number]['Duration']['Help0_Sugg1']['#'] = len(
            df_notification_h0s1.index)
        self.dist_parameter_proact_notification[step_number]['Duration']['Help0_Sugg0']['#'] = len(
            df_notification_h0s0.index)
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help1_Sugg1']['#'] = len(
            df_notification_h1s1.index)
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help1_Sugg0']['#'] = len(
            df_notification_h1s0.index)
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help0_Sugg1']['#'] = len(
            df_notification_h0s1.index)
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help0_Sugg0']['#'] = len(
            df_notification_h0s0.index)

        self.dist_parameter_proact_notification[step_number]['Duration']['Help1_Sugg1']['mean'] = float(
            np.mean(df_notification_h1s1['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Duration']['Help1_Sugg1']['std'] = float(
            np.std(df_notification_h1s1['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Duration']['Help1_Sugg0']['mean'] = float(
            np.mean(df_notification_h1s0['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Duration']['Help1_Sugg0']['std'] = float(
            np.std(df_notification_h1s0['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Duration']['Help0_Sugg1']['mean'] = float(
            np.mean(df_notification_h0s1['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Duration']['Help0_Sugg1']['std'] = float(
            np.std(df_notification_h0s1['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Duration']['Help0_Sugg0']['mean'] = float(
            np.mean(df_notification_h0s0['TimeDurationTask']))
        self.dist_parameter_proact_notification[step_number]['Duration']['Help0_Sugg0']['std'] = float(
            np.std(df_notification_h0s0['TimeDurationTask']))

        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help1_Sugg1']['mean'] = float(
            np.mean(df_notification_h1s1['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help1_Sugg1']['std'] = float(
            np.std(df_notification_h1s1['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help1_Sugg0']['mean'] = float(
            np.mean(df_notification_h1s0['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help1_Sugg0']['std'] = float(
            np.std(df_notification_h1s0['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help0_Sugg1']['mean'] = float(
            np.mean(df_notification_h0s1['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help0_Sugg1']['std'] = float(
            np.std(df_notification_h0s1['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help0_Sugg0']['mean'] = float(
            np.mean(df_notification_h0s0['difficultyTask']))
        self.dist_parameter_proact_notification[step_number]['Difficulty']['Help0_Sugg0']['std'] = float(
            np.std(df_notification_h0s0['difficultyTask']))

        df_suggestion_h1 = self.df_proact_suggestion[step_number][
            self.df_proact_suggestion[step_number]['HelpTask'] == 1]
        df_suggestion_h0 = self.df_proact_suggestion[step_number][
            self.df_proact_suggestion[step_number]['HelpTask'] == 0]
        df_suggestion_h1s1 = df_suggestion_h1[df_suggestion_h1['SuggTask'] == 1]
        df_suggestion_h1s0 = df_suggestion_h1[df_suggestion_h1['SuggTask'] == 0]
        df_suggestion_h0s1 = df_suggestion_h0[df_suggestion_h0['SuggTask'] == 1]
        df_suggestion_h0s0 = df_suggestion_h0[df_suggestion_h0['SuggTask'] == 0]

        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help1_Sugg1']['#'] = len(
            df_suggestion_h1s1.index)
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help1_Sugg0']['#'] = len(
            df_suggestion_h1s0.index)
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help0_Sugg1']['#'] = len(
            df_suggestion_h0s1.index)
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help0_Sugg0']['#'] = len(
            df_suggestion_h0s0.index)
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help1_Sugg1']['#'] = len(
            df_suggestion_h1s1.index)
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help1_Sugg0']['#'] = len(
            df_suggestion_h1s0.index)
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help0_Sugg1']['#'] = len(
            df_suggestion_h0s1.index)
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help0_Sugg0']['#'] = len(
            df_suggestion_h0s0.index)

        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help1_Sugg1']['mean'] = float(
            np.mean(df_suggestion_h1s1['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help1_Sugg1']['std'] = float(
            np.std(df_suggestion_h1s1['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help1_Sugg0']['mean'] = float(
            np.mean(df_suggestion_h1s0['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help1_Sugg0']['std'] = float(
            np.std(df_suggestion_h1s0['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help0_Sugg1']['mean'] = float(
            np.mean(df_suggestion_h0s1['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help0_Sugg1']['std'] = float(
            np.std(df_suggestion_h0s1['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help0_Sugg0']['mean'] = float(
            np.mean(df_suggestion_h0s0['TimeDurationTask']))
        self.dist_parameter_proact_suggestion[step_number]['Duration']['Help0_Sugg0']['std'] = float(
            np.std(df_suggestion_h0s0['TimeDurationTask']))

        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help1_Sugg1']['mean'] = float(
            np.mean(df_suggestion_h1s1['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help1_Sugg1']['std'] = float(
            np.std(df_suggestion_h1s1['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help1_Sugg0']['mean'] = float(
            np.mean(df_suggestion_h1s0['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help1_Sugg0']['std'] = float(
            np.std(df_suggestion_h1s0['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help0_Sugg1']['mean'] = float(
            np.mean(df_suggestion_h0s1['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help0_Sugg1']['std'] = float(
            np.std(df_suggestion_h0s1['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help0_Sugg0']['mean'] = float(
            np.mean(df_suggestion_h0s0['difficultyTask']))
        self.dist_parameter_proact_suggestion[step_number]['Difficulty']['Help0_Sugg0']['std'] = float(
            np.std(df_suggestion_h0s0['difficultyTask']))

        df_intervention_h1 = self.df_proact_intervention[step_number][
            self.df_proact_intervention[step_number]['HelpTask'] == 1]
        df_intervention_h0 = self.df_proact_intervention[step_number][
            self.df_proact_intervention[step_number]['HelpTask'] == 0]
        df_intervention_h1s1 = df_intervention_h1[df_intervention_h1['SuggTask'] == 1]
        df_intervention_h1s0 = df_intervention_h1[df_intervention_h1['SuggTask'] == 0]
        df_intervention_h0s1 = df_intervention_h0[df_intervention_h0['SuggTask'] == 1]
        df_intervention_h0s0 = df_intervention_h0[df_intervention_h0['SuggTask'] == 0]

        self.dist_parameter_proact_intervention[step_number]['Duration']['Help1_Sugg1']['#'] = len(
            df_intervention_h1s1.index)
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help1_Sugg0']['#'] = len(
            df_intervention_h1s0.index)
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help0_Sugg1']['#'] = len(
            df_intervention_h0s1.index)
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help0_Sugg0']['#'] = len(
            df_intervention_h0s0.index)
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help1_Sugg1']['#'] = len(
            df_intervention_h1s1.index)
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help1_Sugg0']['#'] = len(
            df_intervention_h1s0.index)
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help0_Sugg1']['#'] = len(
            df_intervention_h0s1.index)
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help0_Sugg0']['#'] = len(
            df_intervention_h0s0.index)

        self.dist_parameter_proact_intervention[step_number]['Duration']['Help1_Sugg1']['mean'] = float(
            np.mean(df_intervention_h1s1['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help1_Sugg1']['std'] = float(
            np.std(df_intervention_h1s1['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help1_Sugg0']['mean'] = float(
            np.mean(df_intervention_h1s0['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help1_Sugg0']['std'] = float(
            np.std(df_intervention_h1s0['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help0_Sugg1']['mean'] = float(
            np.mean(df_intervention_h0s1['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help0_Sugg1']['std'] = float(
            np.std(df_intervention_h0s1['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help0_Sugg0']['mean'] = float(
            np.mean(df_intervention_h0s0['TimeDurationTask']))
        self.dist_parameter_proact_intervention[step_number]['Duration']['Help0_Sugg0']['std'] = float(
            np.std(df_intervention_h0s0['TimeDurationTask']))

        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help1_Sugg1']['mean'] = float(
            np.mean(df_intervention_h1s1['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help1_Sugg1']['std'] = float(
            np.std(df_intervention_h1s1['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help1_Sugg0']['mean'] = float(
            np.mean(df_intervention_h1s0['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help1_Sugg0']['std'] = float(
            np.std(df_intervention_h1s0['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help0_Sugg1']['mean'] = float(
            np.mean(df_intervention_h0s1['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help0_Sugg1']['std'] = float(
            np.std(df_intervention_h0s1['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help0_Sugg0']['mean'] = float(
            np.mean(df_intervention_h0s0['difficultyTask']))
        self.dist_parameter_proact_intervention[step_number]['Difficulty']['Help0_Sugg0']['std'] = float(
            np.std(df_intervention_h0s0['difficultyTask']))

    def load_all_distribution_parameters(self):
        for step in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
            self.load_distribution_parameter_overall(step)
            self.load_distribution_parameter_correlated(step)
        self.save_dataset_lengths()

    def main(self):
        for p in ('overall', '000', '001', '010', '011', '100', '101', '110', '111'):
            self.load_datasets(personality_values=p)
            self.load_all_distribution_parameters()
            self.dist_parameter[p]['none'] = deepcopy(
                self.dist_parameter_proact_none)
            self.dist_parameter[p]['notification'] = deepcopy(
                self.dist_parameter_proact_notification)
            self.dist_parameter[p]['suggestion'] = deepcopy(
                self.dist_parameter_proact_suggestion)
            self.dist_parameter[p]['intervention'] = deepcopy(
                self.dist_parameter_proact_intervention)
            self.print_len_dist(p)
        # print('Distribution parameter generated...')

        try:
            os.makedirs("user_simulator_data/dist_data")
        except FileExistsError:
            # directory already exists
            pass

        file = open('user_simulator_data/dist_data/dist_data.json', 'w')
        json.dump(self.dist_parameter, file, indent=4, sort_keys=True)
        file.close()

    def print_len_dist(self, p):
        print('###', p, '###', end='\n\n')
        print('none: ', '0:', self.dist_parameter_proact_none['0']['#'],
              '1:', self.dist_parameter_proact_none['1']['#'],
              '2:', self.dist_parameter_proact_none['2']['#'],
              '3:', self.dist_parameter_proact_none['3']['#'],
              '4:', self.dist_parameter_proact_none['4']['#'],
              '5:', self.dist_parameter_proact_none['5']['#'],
              '6:', self.dist_parameter_proact_none['6']['#'],
              '7:', self.dist_parameter_proact_none['7']['#'],
              '8:', self.dist_parameter_proact_none['8']['#'],
              '9:', self.dist_parameter_proact_none['9']['#'],
              '10:', self.dist_parameter_proact_none['10']['#'],
              '11:', self.dist_parameter_proact_none['11']['#'],
              '12:', self.dist_parameter_proact_none['12']['#'], end='\n\n')
        print('notification: ', '0:', self.dist_parameter_proact_notification['0']['#'],
              '1:', self.dist_parameter_proact_notification['1']['#'],
              '2:', self.dist_parameter_proact_notification['2']['#'],
              '3:', self.dist_parameter_proact_notification['3']['#'],
              '4:', self.dist_parameter_proact_notification['4']['#'],
              '5:', self.dist_parameter_proact_notification['5']['#'],
              '6:', self.dist_parameter_proact_notification['6']['#'],
              '7:', self.dist_parameter_proact_notification['7']['#'],
              '8:', self.dist_parameter_proact_notification['8']['#'],
              '9:', self.dist_parameter_proact_notification['9']['#'],
              '10:', self.dist_parameter_proact_notification['10']['#'],
              '11:', self.dist_parameter_proact_notification['11']['#'],
              '12:', self.dist_parameter_proact_notification['12']['#'], end='\n\n')
        print('suggestion: ', '0:', self.dist_parameter_proact_suggestion['0']['#'],
              '1:', self.dist_parameter_proact_suggestion['1']['#'],
              '2:', self.dist_parameter_proact_suggestion['2']['#'],
              '3:', self.dist_parameter_proact_suggestion['3']['#'],
              '4:', self.dist_parameter_proact_suggestion['4']['#'],
              '5:', self.dist_parameter_proact_suggestion['5']['#'],
              '6:', self.dist_parameter_proact_suggestion['6']['#'],
              '7:', self.dist_parameter_proact_suggestion['7']['#'],
              '8:', self.dist_parameter_proact_suggestion['8']['#'],
              '9:', self.dist_parameter_proact_suggestion['9']['#'],
              '10:', self.dist_parameter_proact_suggestion['10']['#'],
              '11:', self.dist_parameter_proact_suggestion['11']['#'],
              '12:', self.dist_parameter_proact_suggestion['12']['#'], end='\n\n')
        print('intervention: ', '0:', self.dist_parameter_proact_intervention['0']['#'],
              '1:', self.dist_parameter_proact_intervention['1']['#'],
              '2:', self.dist_parameter_proact_intervention['2']['#'],
              '3:', self.dist_parameter_proact_intervention['3']['#'],
              '4:', self.dist_parameter_proact_intervention['4']['#'],
              '5:', self.dist_parameter_proact_intervention['5']['#'],
              '6:', self.dist_parameter_proact_intervention['6']['#'],
              '7:', self.dist_parameter_proact_intervention['7']['#'],
              '8:', self.dist_parameter_proact_intervention['8']['#'],
              '9:', self.dist_parameter_proact_intervention['9']['#'],
              '10:', self.dist_parameter_proact_intervention['10']['#'],
              '11:', self.dist_parameter_proact_intervention['11']['#'],
              '12:', self.dist_parameter_proact_intervention['12']['#'], end='\n\n\n')

    def print_len_temp_dataset(self, p):
        print('###', p, '###', end='\n\n')
        print('none: ', '0:', len(self.df_proact_none['0'].index),
              '1:', len(self.df_proact_none['1'].index),
              '2:', len(self.df_proact_none['2'].index),
              '3:', len(self.df_proact_none['3'].index),
              '4:', len(self.df_proact_none['4'].index),
              '5:', len(self.df_proact_none['5'].index),
              '6:', len(self.df_proact_none['6'].index),
              '7:', len(self.df_proact_none['7'].index),
              '8:', len(self.df_proact_none['8'].index),
              '9:', len(self.df_proact_none['9'].index),
              '10:', len(self.df_proact_none['10'].index),
              '11:', len(self.df_proact_none['11'].index),
              '12:', len(self.df_proact_none['12'].index), end='\n\n')
        print('notification: ', '0:', len(self.df_proact_notification['0'].index),
              '1:', len(self.df_proact_notification['1'].index),
              '2:', len(self.df_proact_notification['2'].index),
              '3:', len(self.df_proact_notification['3'].index),
              '4:', len(self.df_proact_notification['4'].index),
              '5:', len(self.df_proact_notification['5'].index),
              '6:', len(self.df_proact_notification['6'].index),
              '7:', len(self.df_proact_notification['7'].index),
              '8:', len(self.df_proact_notification['8'].index),
              '9:', len(self.df_proact_notification['9'].index),
              '10:', len(self.df_proact_notification['10'].index),
              '11:', len(self.df_proact_notification['11'].index),
              '12:', len(self.df_proact_notification['12'].index), end='\n\n')
        print('suggestion: ', '0:', len(self.df_proact_suggestion['0'].index),
              '1:', len(self.df_proact_suggestion['1'].index),
              '2:', len(self.df_proact_suggestion['2'].index),
              '3:', len(self.df_proact_suggestion['3'].index),
              '4:', len(self.df_proact_suggestion['4'].index),
              '5:', len(self.df_proact_suggestion['5'].index),
              '6:', len(self.df_proact_suggestion['6'].index),
              '7:', len(self.df_proact_suggestion['7'].index),
              '8:', len(self.df_proact_suggestion['8'].index),
              '9:', len(self.df_proact_suggestion['9'].index),
              '10:', len(self.df_proact_suggestion['10'].index),
              '11:', len(self.df_proact_suggestion['11'].index),
              '12:', len(self.df_proact_suggestion['12'].index), end='\n\n')
        print('intervention: ', '0:', len(self.df_proact_intervention['0'].index),
              '1:', len(self.df_proact_intervention['1'].index),
              '2:', len(self.df_proact_intervention['2'].index),
              '3:', len(self.df_proact_intervention['3'].index),
              '4:', len(self.df_proact_intervention['4'].index),
              '5:', len(self.df_proact_intervention['5'].index),
              '6:', len(self.df_proact_intervention['6'].index),
              '7:', len(self.df_proact_intervention['7'].index),
              '8:', len(self.df_proact_intervention['8'].index),
              '9:', len(self.df_proact_intervention['9'].index),
              '10:', len(self.df_proact_intervention['10'].index),
              '11:', len(self.df_proact_intervention['11'].index),
              '12:', len(self.df_proact_intervention['12'].index), end='\n\n\n')


if __name__ == '__main__':
    obj = DistributionParameter()
    obj.main()
    print('Finished... You can start simulating!')
