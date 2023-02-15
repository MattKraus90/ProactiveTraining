import pandas as pd
#
# pds = personalDetails.PersonalDetails()
# pds.generate_person_data()
# li = []
# t1 = datetime.now()
# for i in range(1000):
#     pds.generate_person_data()
#     li.append(pd.pers_data['preTrust'])
# print(datetime.now() - t1)
# plt.hist(li, density=True, bins=100)
# plt.show()
#
# sD = simData.SimData()
# sD.set_proactivity([0, 0, 0, 1])
# sD.set_complexity('3')
# sD.generate_values()
# print(sD.simulated_step_data)
# li = []
# li2 = []
# t1 = datetime.now()
# for i in range(1000):
#     sD.gen_duration()
#     li.append(sD.simulated_step_data['duration'])
#     sD.gen_difficulty()
#     li2.append(sD.simulated_step_data['difficulty'])
#     # print(sD.simulated_step_data['duration'])
#     # print(sD.simulated_step_data['difficulty'])
# print(datetime.now() - t1)
# plt.hist(li, density=True, bins=100)
# plt.show()
# plt.hist(li2, density=True, bins=100)
# plt.show()
#
# """ t h&l
#     p h&l
#     m h&l
#     111 -> 2^3 =
#     000
#     001
#     010
#     011
#     100
#     101
#     110
#     """

# df = pd.read_csv('dataSummary.csv')
# df = df.reindex(sorted(df.columns), axis=1)
#
# df_none = df[df['ProactiveTask' + str(3)] == 'Notification']
# # df_none_sort1 = df_none[df_none['Technical Affinity'] > 3.0]
# # df_none_sort2 = df_none[df_none['PreTrust'] <= 3.0]
# # df_none_sort3 = df_none[df_none['ExperienceManagement'] <= 3.0]
# df_none_sort1 = df_none[df_none['Technical Affinity'] <= 3.0]
# df_none_sort2 = df_none_sort1[df_none_sort1['PreTrust'] <= 3.0]
# df_none_sort3 = df_none_sort2[df_none_sort2['ExperienceManagement'] <= 3.0]
# print('000', len(df_none_sort3.index))
# df_none_sort1 = df_none[df_none['Technical Affinity'] <= 3.0]
# df_none_sort2 = df_none_sort1[df_none_sort1['PreTrust'] <= 3.0]
# df_none_sort3 = df_none_sort2[df_none_sort2['ExperienceManagement'] > 3.0]
# print('001', len(df_none_sort3.index))
# df_none_sort1 = df_none[df_none['Technical Affinity'] <= 3.0]
# df_none_sort2 = df_none_sort1[df_none_sort1['PreTrust'] > 3.0]
# df_none_sort3 = df_none_sort2[df_none_sort2['ExperienceManagement'] <= 3.0]
# print('010', len(df_none_sort3.index))
# df_none_sort1 = df_none[df_none['Technical Affinity'] <= 3.0]
# df_none_sort2 = df_none_sort1[df_none_sort1['PreTrust'] > 3.0]
# df_none_sort3 = df_none_sort2[df_none_sort2['ExperienceManagement'] > 3.0]
# print('011', len(df_none_sort3.index))
# df_none_sort1 = df_none[df_none['Technical Affinity'] > 3.0]
# df_none_sort2 = df_none_sort1[df_none_sort1['PreTrust'] <= 3.0]
# df_none_sort3 = df_none_sort2[df_none_sort2['ExperienceManagement'] <= 3.0]
# print('100', len(df_none_sort3.index))
# df_none_sort1 = df_none[df_none['Technical Affinity'] > 3.0]
# df_none_sort2 = df_none_sort1[df_none_sort1['PreTrust'] <= 3.0]
# df_none_sort3 = df_none_sort2[df_none_sort2['ExperienceManagement'] > 3.0]
# print('101', len(df_none_sort3.index))
# df_none_sort1 = df_none[df_none['Technical Affinity'] > 3.0]
# df_none_sort2 = df_none_sort1[df_none_sort1['PreTrust'] > 3.0]
# df_none_sort3 = df_none_sort2[df_none_sort2['ExperienceManagement'] <= 3.0]
# print('110', len(df_none_sort3.index))
# df_none_sort1 = df_none[df_none['Technical Affinity'] > 3.0]
# df_none_sort2 = df_none_sort1[df_none_sort1['PreTrust'] > 3.0]
# df_none_sort3 = df_none_sort2[df_none_sort2['ExperienceManagement'] > 3.0]
# # print(len(df_none_sort1.index))
# # print(len(df_none_sort2.index))
# print('111', len(df_none_sort3.index))

# for p in ('000', '001', '010', '011', '100', '101', '110', '111'):
#     if p[0] == '0':
#         df_sorted_1 = df_none[df_none['ExperienceManagement'] <= 3.0]
#     else:
#         df_sorted_1 = df_none[df_none['ExperienceManagement'] > 3.0]
#     if p[1] == '0':
#         df_sorted_2 = df_sorted_1[df_sorted_1['PreTrust'] <= 3.0]
#     else:
#         df_sorted_2 = df_sorted_1[df_sorted_1['PreTrust'] > 3.0]
#     if p[2] == '0':
#         df_sorted_3 = df_sorted_2[df_sorted_2['Technical Affinity'] <= 3.0]
#     else:
#         df_sorted_3 = df_sorted_2[df_sorted_2['Technical Affinity'] > 3.0]
#
#     print(p, len(df_sorted_3.index))
#
# for p in ('000', '001', '010', '011', '100', '101', '110', '111'):
#     if p[0] == '0':
#         df_sorted_1 = df_none[df_none['Technical Affinity'] <= 3.0]
#     else:
#         df_sorted_1 = df_none[df_none['Technical Affinity'] > 3.0]
#     if p[1] == '0':
#         df_sorted_2 = df_sorted_1[df_sorted_1['PreTrust'] <= 3.0]
#     else:
#         df_sorted_2 = df_sorted_1[df_sorted_1['PreTrust'] > 3.0]
#     if p[2] == '0':
#         df_sorted_3 = df_sorted_2[df_sorted_2['ExperienceManagement'] <= 3.0]
#     else:
#         df_sorted_3 = df_sorted_2[df_sorted_2['ExperienceManagement'] > 3.0]
#
#     print('##', p, len(df_sorted_3.index))
# import json
#
# file = open('user_simulator_data/dist_data/dist_data_personality.json', 'r')
# dist_parameter = json.load(file)
# print(dist_parameter)
#
# df_whole = pd.read_csv('dataSummary.csv')
# df_whole = df_whole.reindex(sorted(df_whole.columns), axis=1)
#
# # for i in range(1, 13):
# #     print(df_whole['pointsTask' + str(i)].value_counts(), end='\n\n\n')
# for i in range(1, 13):
#     df = df_whole['pointsTask' + str(i)].value_counts(normalize=True)
#     print(df.get(10), end='\n\n')

# import distribution_parameter_dict
# distribution_parameter_obj = distribution_parameter_dict.DistParameterDataStructures()
# dist_parameter_points = distribution_parameter_obj.dist_parameter_points
# keys = dist_parameter_points['overall']['none']['1']['Help0_Sugg0'].keys()
# print(keys)

# d = {'age': [0.0], 'gender': [''], 'technical affinity': [0.0], 'management experience': [0.0],
#      'preTrust': [0.0], 'neuroticism': [0.0], 'extraversion': [0.0], 'openness': [0.0],
#      'agreeableness': [0.0], 'conscientiousness': [0.0]}
# d2 = {'age': [1.0], 'technical affinity': [1.0], 'management experience': [1.0],
#       'preTrust': [2.0], 'neuroticism': [2.0], 'extraversion': [2.0], 'openness': [2.0],
#       'agreeableness': [2.0], 'conscientiousness': [2.0]}
#
# df = pd.DataFrame()
# df['age'] = [3.0]
# df['gender'] = ['other']
# df['technical affinity'] = [4.0]
# df['management experience'] = [3.0]
# df['preTrust'] = [3.0]
# df['neuroticism'] = [3.0]
# df['extraversion'] = [3.0]
# df['openness'] = [3.0]
# df['agreeableness'] = [3.0]
# df['conscientiousness'] = [3.0]
#
# df = df.append(pd.DataFrame(d2))
#
# print(df)
#
# df.to_csv('user_simulator_data/simulated_data/test.csv')

import pickle
import numpy as np

#
# with open("misc/Trust-Schätzer/svm_trust_Model.pkl", 'rb') as file:
#     Pickled_LR_Model = pickle.load(file)
#
# print(type(Pickled_LR_Model))
# print(Pickled_LR_Model)
# # input_vector = [
# #     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
# #      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0, 0, 0, 0.7071067811865475, -0.7071067811865475, 1, 0,
# #      0, 0, 1, 0, 1, -0.7071067811865475, 0.9352129574085184, 0.9428090415820631, 0.7071067811865475,
# #      1.6364428945074108, 0, 1, 0, 0.47140452079103157, -0.7071067811865475, 0.0, 0.0, 0.7071067811865475,
# #      1.414213562373095]]
#
# input_vector = [
#     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
#      0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0, 0.8899999999999999, 9.0, 1, 0, 0, 0, 1, 0, 1, 9.0, 21.33, 3.71,
#      2.14, 40.85, 0, 1, 0, 0.33000000000000007, 1.7999999999999998, 3.59, 2.22, 0.72, 1.9700000000000002]
#     ]
#
# result = Pickled_LR_Model.predict(input_vector)
# print(result)
# # print(Pickled_LR_Model.get_params())

# df = pd.read_csv('dataSummary.csv')
# df = df.reindex(sorted(df.columns), axis=1)
#
# duration_task_mean = []
# duration_task_std = []
# task = 1
# print(df['TimeDurationTask' + str(task)])
# mean = df['TimeDurationTask' + str(task)].mean()
# std = df['TimeDurationTask' + str(task)].std()
# duration_task_mean.append(mean)
# duration_task_std.append(std)
#
# print(duration_task_mean)
# print(duration_task_std)

# import configparser
#
# parser = configparser.ConfigParser()
#
# parser.read('Config.ini')
#
# c = 0
# for v in parser['Proactivity_Strategy'].values():
#     if v != 'False':
#         c += 1

# proactivity_df = pd.read_csv('misc/DataAnalysis/proactivity_gt.csv')
# print(proactivity_df.loc[0, 'ProactiveTask' + str(1)].lower())
#
# df = pd.read_csv('dataSummary.csv')
# df = df.reindex(sorted(df.columns), axis=1)
#
# tmp = df.loc[:,
#       ['ProactiveTask' + str(1), 'TimeDurationTask' + str(1), 'difficultyTask' + str(1),
#        'pointsTask' + str(1), 'HelpTask' + str(1), 'SuggTask' + str(1),
#        'TrustTask' + str(1)]]
#
# print(tmp.to_string())

df_none = pd.read_csv('user_simulator_data/results/step_number_results_only_none_2021_10_02_13_10_13.csv')
df_notification = pd.read_csv(
    'user_simulator_data/results/step_number_results_only_notification_2021_10_02_13_14_49.csv')
df_suggestion = pd.read_csv('user_simulator_data/results/step_number_results_only_suggestion_2021_10_02_13_20_08.csv')
df_intervention = pd.read_csv(
    'user_simulator_data/results/step_number_results_only_intervention_2021_10_02_13_24_51.csv')
df_adaptive = pd.read_csv('user_simulator_data/results/step_number_results_Strategy_Adaptive_2021_10_02_13_29_12.csv')

df = pd.DataFrame()
df = df.append(df_none)
df = df.append(df_notification)
df = df.append(df_suggestion)
df = df.append(df_intervention)
df = df.append(df_adaptive)

df.to_csv('user_simulator_data/results/step_number_results.csv')
