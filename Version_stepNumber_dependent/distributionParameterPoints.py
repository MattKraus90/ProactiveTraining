import pandas as pd
import json

import distribution_parameter_dict


class DistributionParameterPoints:
    def __init__(self):
        distribution_parameter_obj = distribution_parameter_dict.DistParameterDataStructures()
        self.dist_parameter_points = distribution_parameter_obj.dist_parameter_points

        self.df_points = {
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

        self.load_datasets()

    def load_datasets(self):
        df_whole = pd.read_csv('dataSummary.csv')
        df_whole = df_whole.reindex(sorted(df_whole.columns), axis=1)

        for p in ('overall', '000', '001', '010', '011', '100', '101', '110', '111'):
            if p == 'overall':
                df = df_whole.copy()
            else:
                if p[0] == '0':
                    df_sorted_1 = df_whole[df_whole['ExperienceManagement'] <= 3.0]
                else:
                    df_sorted_1 = df_whole[df_whole['ExperienceManagement'] > 3.0]
                if p[1] == '0':
                    df_sorted_2 = df_sorted_1[df_sorted_1['PreTrust'] <= 3.0]
                else:
                    df_sorted_2 = df_sorted_1[df_sorted_1['PreTrust'] > 3.0]
                if p[2] == '0':
                    df_sorted_3 = df_sorted_2[df_sorted_2['Technical Affinity'] <= 3.0]
                else:
                    df_sorted_3 = df_sorted_2[df_sorted_2['Technical Affinity'] > 3.0]
                df = df_sorted_3

            for s in range(1, 13):
                for proactivity in ('None', 'Notification', 'Suggestion', 'Intervention'):
                    df_proactivity = df[df['ProactiveTask' + str(s)] == proactivity]
                    df_sort_out = df_proactivity.loc[:,
                                  ['ProactiveTask' + str(s), 'TimeDurationTask' + str(s), 'difficultyTask' + str(s),
                                   'pointsTask' + str(s), 'HelpTask' + str(s), 'SuggTask' + str(s),
                                   'TrustTask' + str(s)]]

                    self.df_points[p][proactivity.lower()][str(s)] = df_sort_out

    def calculate_distribution_parameter(self):
        for p in ('overall', '000', '001', '010', '011', '100', '101', '110', '111'):
            for s in range(1, 13):
                for proactivity in ('none', 'notification', 'suggestion', 'intervention'):
                    df = self.df_points[p][proactivity][str(s)]
                    df_h1 = df[df['HelpTask' + str(s)] == 1]
                    df_h0 = df[df['HelpTask' + str(s)] == 0]
                    df_h1s1 = df_h1[df_h1['SuggTask' + str(s)] == 1]
                    df_h1s0 = df_h1[df_h1['SuggTask' + str(s)] == 0]
                    df_h0s1 = df_h0[df_h0['SuggTask' + str(s)] == 1]
                    df_h0s0 = df_h0[df_h0['SuggTask' + str(s)] == 0]

                    self.dist_parameter_points[p][proactivity][str(s)]['overall']['#'] = len(df.index)
                    self.dist_parameter_points[p][proactivity][str(s)]['Help1_Sugg1']['#'] = len(df_h1s1.index)
                    self.dist_parameter_points[p][proactivity][str(s)]['Help1_Sugg0']['#'] = len(df_h1s0.index)
                    self.dist_parameter_points[p][proactivity][str(s)]['Help0_Sugg1']['#'] = len(df_h0s1.index)
                    self.dist_parameter_points[p][proactivity][str(s)]['Help0_Sugg0']['#'] = len(df_h0s0.index)

                    len_dict = len(self.dist_parameter_points[p][proactivity][str(s)]['Help0_Sugg0'])
                    points = (0, 10, 20, 30, 40)

                    v_all = df['pointsTask' + str(s)].value_counts(normalize=True)
                    v_h1s1 = df_h1s1['pointsTask' + str(s)].value_counts(normalize=True)
                    v_h1s0 = df_h1s0['pointsTask' + str(s)].value_counts(normalize=True)
                    v_h0s1 = df_h0s1['pointsTask' + str(s)].value_counts(normalize=True)
                    v_h0s0 = df_h0s0['pointsTask' + str(s)].value_counts(normalize=True)

                    for i in range(0, len_dict - 1):
                        # print(p, proactivity, s, i, 'points[i]: ', points[i], 'v_h1s1.get(points[i])',
                        #       v_h1s1.get(points[i]), 'len_dataset:', len(df_h1s1.index))
                        if v_h1s1.get(points[i]):
                            self.dist_parameter_points[p][proactivity][str(s)]['Help1_Sugg1'][
                                'points_' + str(points[i])] = v_h1s1.get(points[i])
                        else:
                            self.dist_parameter_points[p][proactivity][str(s)]['Help1_Sugg1'][
                                'points_' + str(points[i])] = 0.0

                        if v_h1s0.get(points[i]):
                            self.dist_parameter_points[p][proactivity][str(s)]['Help1_Sugg0'][
                                'points_' + str(points[i])] = v_h1s0.get(points[i])
                        else:
                            self.dist_parameter_points[p][proactivity][str(s)]['Help1_Sugg0'][
                                'points_' + str(points[i])] = 0.0

                        if v_h0s1.get(points[i]):
                            self.dist_parameter_points[p][proactivity][str(s)]['Help0_Sugg1'][
                                'points_' + str(points[i])] = v_h0s1.get(points[i])
                        else:
                            self.dist_parameter_points[p][proactivity][str(s)]['Help0_Sugg1'][
                                'points_' + str(points[i])] = 0.0

                        if v_h0s0.get(points[i]):
                            self.dist_parameter_points[p][proactivity][str(s)]['Help0_Sugg0'][
                                'points_' + str(points[i])] = v_h0s0.get(points[i])
                        else:
                            self.dist_parameter_points[p][proactivity][str(s)]['Help0_Sugg0'][
                                'points_' + str(points[i])] = 0.0

                        if v_all.get(points[i]):
                            self.dist_parameter_points[p][proactivity][str(s)]['overall'][
                                'points_' + str(points[i])] = v_all.get(points[i])
                        else:
                            self.dist_parameter_points[p][proactivity][str(s)]['overall'][
                                'points_' + str(points[i])] = 0.0

    def save_dist_parameter(self):
        file = open('user_simulator_data/dist_data/dist_data_points.json', 'w')
        json.dump(self.dist_parameter_points, file, indent=4, sort_keys=True)
        file.close()


if __name__ == '__main__':
    o = DistributionParameterPoints()
    o.calculate_distribution_parameter()
    o.save_dist_parameter()
