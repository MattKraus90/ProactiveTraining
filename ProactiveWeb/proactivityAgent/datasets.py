import os

import pandas as pd

DIRECTORY_PATH = os.path.dirname(__file__)


class GenDatasets:
    def __init__(self):# Punkteberechnung:
#         meine seite / java seite
#     1A: 180/210     / 190/210
#     1B: 200/210     / 190/210
#     1C: 190/210     / 200/210
        self.df_whole = pd.read_csv(os.path.join(
            DIRECTORY_PATH, 'data/dataSummary.csv'))
        self.df_whole = self.df_whole.reindex(
            sorted(self.df_whole.columns), axis=1)
        self.df = pd.DataFrame()

        self.df_dict = {
            'overall': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                 '4': pd.DataFrame(),
                                 '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                 '8': pd.DataFrame(),
                                 '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                 '12': pd.DataFrame()},
                        'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                         '4': pd.DataFrame(),
                                         '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                         '8': pd.DataFrame(),
                                         '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                         '12': pd.DataFrame()},
                        'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                       '4': pd.DataFrame(),
                                       '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                       '8': pd.DataFrame(),
                                       '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                       '12': pd.DataFrame()},
                        'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                         '4': pd.DataFrame(),
                                         '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                         '8': pd.DataFrame(),
                                         '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                         '12': pd.DataFrame()}
                        },
            '000': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                             '4': pd.DataFrame(),
                             '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                             '8': pd.DataFrame(),
                             '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                             '12': pd.DataFrame()},
                    'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()},
                    'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                   '4': pd.DataFrame(),
                                   '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                   '8': pd.DataFrame(),
                                   '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                   '12': pd.DataFrame()},
                    'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
                    },
            '001': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                             '4': pd.DataFrame(),
                             '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                             '8': pd.DataFrame(),
                             '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                             '12': pd.DataFrame()},
                    'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()},
                    'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                   '4': pd.DataFrame(),
                                   '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                   '8': pd.DataFrame(),
                                   '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                   '12': pd.DataFrame()},
                    'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
                    },
            '010': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                             '4': pd.DataFrame(),
                             '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                             '8': pd.DataFrame(),
                             '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                             '12': pd.DataFrame()},
                    'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()},
                    'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                   '4': pd.DataFrame(),
                                   '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                   '8': pd.DataFrame(),
                                   '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                   '12': pd.DataFrame()},
                    'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
                    },
            '011': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                             '4': pd.DataFrame(),
                             '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                             '8': pd.DataFrame(),
                             '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                             '12': pd.DataFrame()},
                    'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()},
                    'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                   '4': pd.DataFrame(),
                                   '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                   '8': pd.DataFrame(),
                                   '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                   '12': pd.DataFrame()},
                    'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
                    },
            '100': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                             '4': pd.DataFrame(),
                             '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                             '8': pd.DataFrame(),
                             '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                             '12': pd.DataFrame()},
                    'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()},
                    'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                   '4': pd.DataFrame(),
                                   '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                   '8': pd.DataFrame(),
                                   '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                   '12': pd.DataFrame()},
                    'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
                    },
            '101': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                             '4': pd.DataFrame(),
                             '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                             '8': pd.DataFrame(),
                             '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                             '12': pd.DataFrame()},
                    'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()},
                    'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                   '4': pd.DataFrame(),
                                   '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                   '8': pd.DataFrame(),
                                   '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                   '12': pd.DataFrame()},
                    'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
                    },
            '110': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                             '4': pd.DataFrame(),
                             '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                             '8': pd.DataFrame(),
                             '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                             '12': pd.DataFrame()},
                    'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()},
                    'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                   '4': pd.DataFrame(),
                                   '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                   '8': pd.DataFrame(),
                                   '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                   '12': pd.DataFrame()},
                    'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
                    },
            '111': {'none': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                             '4': pd.DataFrame(),
                             '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                             '8': pd.DataFrame(),
                             '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                             '12': pd.DataFrame()},
                    'notification': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()},
                    'suggestion': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                   '4': pd.DataFrame(),
                                   '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                   '8': pd.DataFrame(),
                                   '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                   '12': pd.DataFrame()},
                    'intervention': {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
                    }
        }

        self.df_proact_none = {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                               '4': pd.DataFrame(),
                               '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                               '8': pd.DataFrame(),
                               '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                               '12': pd.DataFrame()}
        self.df_proact_notification = {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                       '4': pd.DataFrame(),
                                       '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                       '8': pd.DataFrame(),
                                       '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                       '12': pd.DataFrame()}
        self.df_proact_suggestion = {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                     '4': pd.DataFrame(),
                                     '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                     '8': pd.DataFrame(),
                                     '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                     '12': pd.DataFrame()}
        self.df_proact_intervention = {'1': pd.DataFrame(), '2': pd.DataFrame(), '3': pd.DataFrame(),
                                       '4': pd.DataFrame(),
                                       '5': pd.DataFrame(), '6': pd.DataFrame(), '7': pd.DataFrame(),
                                       '8': pd.DataFrame(),
                                       '9': pd.DataFrame(), '10': pd.DataFrame(), '11': pd.DataFrame(),
                                       '12': pd.DataFrame()}

        self.generate_dependency_of_datasets_from_personality_attributes()

    def generate_separated_dataframes_without_step_number(self):
        """generates separated DataFrames for the different proactivity values
        (None, Notification, Suggestion, Intervention).
        Concatenates the values from all 12 steps (neglects complexity)"""

        self.df_proact_none['0'] = pd.DataFrame(
            columns=['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask', 'SuggTask',
                     'TrustTask'])
        self.df_proact_notification['0'] = pd.DataFrame(
            columns=['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask', 'SuggTask',
                     'TrustTask'])
        self.df_proact_suggestion['0'] = pd.DataFrame(
            columns=['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask', 'SuggTask',
                     'TrustTask'])
        self.df_proact_intervention['0'] = pd.DataFrame(
            columns=['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask', 'SuggTask',
                     'TrustTask'])

        for i in range(1, 13):
            df_none = self.df[self.df['ProactiveTask' + str(i)] == 'None']
            df_sort_out = df_none.loc[:,
                                      ['ProactiveTask' + str(i), 'TimeDurationTask' + str(i), 'difficultyTask' + str(i),
                                       'pointsTask' + str(i), 'HelpTask' +
                                       str(i), 'SuggTask' + str(i),
                                       'TrustTask' + str(i)]]

            df_sort_out.columns = ['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask',
                                   'SuggTask', 'TrustTask']

            self.df_proact_none['0'] = pd.concat(
                [self.df_proact_none['0'], df_sort_out])

        for i in range(1, 13):
            df_notification = self.df[self.df['ProactiveTask' +
                                              str(i)] == 'Notification']
            df_sort_out = df_notification.loc[:,
                                              ['ProactiveTask' + str(i), 'TimeDurationTask' + str(i), 'difficultyTask' + str(i),
                                               'pointsTask' + str(i), 'HelpTask' +
                                                  str(i), 'SuggTask' + str(i),
                                                  'TrustTask' + str(i)]]

            df_sort_out.columns = ['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask',
                                   'SuggTask', 'TrustTask']

            self.df_proact_notification['0'] = pd.concat(
                [self.df_proact_notification['0'], df_sort_out])

        for i in range(1, 13):
            df_suggestion = self.df[self.df['ProactiveTask' +
                                            str(i)] == 'Suggestion']
            df_sort_out = df_suggestion.loc[:,
                                            ['ProactiveTask' + str(i), 'TimeDurationTask' + str(i), 'difficultyTask' + str(i),
                                             'pointsTask' + str(i), 'HelpTask' +
                                             str(i), 'SuggTask' + str(i),
                                             'TrustTask' + str(i)]]

            df_sort_out.columns = ['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask',
                                   'SuggTask', 'TrustTask']

            self.df_proact_suggestion['0'] = pd.concat(
                [self.df_proact_suggestion['0'], df_sort_out])

        for i in range(1, 13):
            df_intervention = self.df[self.df['ProactiveTask' +
                                              str(i)] == 'Intervention']
            df_sort_out = df_intervention.loc[:,
                                              ['ProactiveTask' + str(i), 'TimeDurationTask' + str(i), 'difficultyTask' + str(i),
                                               'pointsTask' + str(i), 'HelpTask' +
                                                  str(i), 'SuggTask' + str(i),
                                                  'TrustTask' + str(i)]]

            df_sort_out.columns = ['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask',
                                   'SuggTask', 'TrustTask']

            self.df_proact_intervention['0'] = pd.concat(
                [self.df_proact_intervention['0'], df_sort_out])

        # self.df_proact_none.to_csv('Test/concat_test_none.csv')
        # self.df_proact_notification.to_csv('Test/concat_test_notification.csv')
        # self.df_proact_suggestion.to_csv('Test/concat_test_suggestion.csv')
        # self.df_proact_intervention.to_csv('Test/concat_test_intervention.csv')
        # print(self.df_proact_none)

    def generate_separated_dataframes_with_step_number(self):
        """generates separated DataFrames for the different proactivity values
        (None, Notification, Suggestion, Intervention)."""

        for i in range(1, 13):
            df_none = self.df[self.df['ProactiveTask' + str(i)] == 'None']
            df_sort_out = df_none.loc[:,
                                      ['ProactiveTask' + str(i), 'TimeDurationTask' + str(i), 'difficultyTask' + str(i),
                                       'pointsTask' + str(i), 'HelpTask' +
                                       str(i), 'SuggTask' + str(i),
                                       'TrustTask' + str(i)]]

            df_sort_out.columns = ['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask',
                                   'SuggTask', 'TrustTask']

            self.df_proact_none[str(i)] = df_sort_out.copy()

        for i in range(1, 13):
            df_notification = self.df[self.df['ProactiveTask' +
                                              str(i)] == 'Notification']
            df_sort_out = df_notification.loc[:,
                                              ['ProactiveTask' + str(i), 'TimeDurationTask' + str(i), 'difficultyTask' + str(i),
                                               'pointsTask' + str(i), 'HelpTask' +
                                                  str(i), 'SuggTask' + str(i),
                                                  'TrustTask' + str(i)]]

            df_sort_out.columns = ['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask',
                                   'SuggTask', 'TrustTask']

            self.df_proact_notification[str(i)] = df_sort_out.copy()

        for i in range(1, 13):
            df_suggestion = self.df[self.df['ProactiveTask' +
                                            str(i)] == 'Suggestion']
            df_sort_out = df_suggestion.loc[:,
                                            ['ProactiveTask' + str(i), 'TimeDurationTask' + str(i), 'difficultyTask' + str(i),
                                             'pointsTask' + str(i), 'HelpTask' +
                                             str(i), 'SuggTask' + str(i),
                                             'TrustTask' + str(i)]]

            df_sort_out.columns = ['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask',
                                   'SuggTask', 'TrustTask']

            self.df_proact_suggestion[str(i)] = df_sort_out.copy()

        for i in range(1, 13):
            df_intervention = self.df[self.df['ProactiveTask' +
                                              str(i)] == 'Intervention']
            df_sort_out = df_intervention.loc[:,
                                              ['ProactiveTask' + str(i), 'TimeDurationTask' + str(i), 'difficultyTask' + str(i),
                                               'pointsTask' + str(i), 'HelpTask' +
                                                  str(i), 'SuggTask' + str(i),
                                                  'TrustTask' + str(i)]]

            df_sort_out.columns = ['ProactiveTask', 'TimeDurationTask', 'difficultyTask', 'pointsTask', 'HelpTask',
                                   'SuggTask', 'TrustTask']

            self.df_proact_intervention[str(i)] = df_sort_out.copy()

        # self.df_proact_none.to_csv('Test/test_none.csv')
        # self.df_proact_notification.to_csv('Test/test_notification.csv')
        # self.df_proact_suggestion.to_csv('Test/test_suggestion.csv')
        # self.df_proact_intervention.to_csv('Test/test_intervention.csv')

    def generate_dependency_of_datasets_from_personality_attributes(self):
        """makes datasets dependent from 'management experience', 'preTrust' and 'technical affinity'"""
        for p in ('overall', '000', '001', '010', '011', '100', '101', '110', '111'):
            if p == 'overall':
                self.df = self.df_whole.copy()
            else:
                if p[0] == '0':
                    df_sorted_1 = self.df_whole[self.df_whole['ExperienceManagement'] <= 3.0]
                else:
                    df_sorted_1 = self.df_whole[self.df_whole['ExperienceManagement'] > 3.0]
                if p[1] == '0':
                    df_sorted_2 = df_sorted_1[df_sorted_1['PreTrust'] <= 3.0]
                else:
                    df_sorted_2 = df_sorted_1[df_sorted_1['PreTrust'] > 3.0]
                if p[2] == '0':
                    df_sorted_3 = df_sorted_2[df_sorted_2['Technical Affinity'] <= 3.0]
                else:
                    df_sorted_3 = df_sorted_2[df_sorted_2['Technical Affinity'] > 3.0]
                self.df = df_sorted_3

            self.generate_separated_dataframes_without_step_number()
            self.generate_separated_dataframes_with_step_number()
            self.df_dict[p]['none'] = self.df_proact_none.copy()
            self.df_dict[p]['notification'] = self.df_proact_notification.copy()
            self.df_dict[p]['suggestion'] = self.df_proact_suggestion.copy()
            self.df_dict[p]['intervention'] = self.df_proact_intervention.copy()
            # self.print_len_temp_dataset(p=p)
        # print('Datasets created...')

    def print_len_temp_dataset(self, p):
        print('###', p, '###', end='\n\n')
        print('none: ', '0:', len(self.df_proact_none['1'].index),
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

    # def print_len_big_dataset(self):
    #     for p in ('overall', '000', '001', '010', '011', '100', '101', '110', '111'):
    #         print('###', p, '###', end='\n\n')
    #         print('none: ', '0:', len(self.df_dict[p]['none']['0'].index),
    #               '3:', len(self.df_dict[p]['none']['3'].index),
    #               '4:', len(self.df_dict[p]['none']['4'].index),
    #               '5:', len(self.df_dict[p]['none']['5'].index), end='\n\n')
    #         print('notification: ', '0:', len(self.df_dict[p]['notification']['0'].index),
    #               '3:', len(self.df_dict[p]['notification']['3'].index),
    #               '4:', len(self.df_dict[p]['notification']['4'].index),
    #               '5:', len(self.df_dict[p]['notification']['5'].index), end='\n\n')
    #         print('suggestion: ', '0:', len(self.df_dict[p]['suggestion']['0'].index),
    #               '3:', len(self.df_dict[p]['suggestion']['3'].index),
    #               '4:', len(self.df_dict[p]['suggestion']['4'].index),
    #               '5:', len(self.df_dict[p]['suggestion']['5'].index), end='\n\n')
    #         print('intervention: ', '0:', len(self.df_dict[p]['intervention']['0'].index),
    #               '3:', len(self.df_dict[p]['intervention']['3'].index),
    #               '4:', len(self.df_dict[p]['intervention']['4'].index),
    #               '5:', len(self.df_dict[p]['intervention']['5'].index), end='\n\n\n')


if __name__ == '__main__':
    from datetime import datetime

    t1 = datetime.now()
    obj = GenDatasets()
    t2 = datetime.now()
    print(t2 - t1)

    # obj.print_len_big_dataset()
