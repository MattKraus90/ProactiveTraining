import json
import os
import random

from django.templatetags.static import static

# Punkteberechnung:
#         meine seite / java seite
#     1A: 180/210     / 190/210
#     1B: 200/210     / 190/210
#     1C: 190/210     / 200/210

def read_json(filename: str):
    path = static('json/' + filename)
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except:
        data = {}
        
    return data


def write_json(filename: str, data):
    path = static('json/' + filename)
    with open(path, 'w') as f:
        f.write(data)


def remove_json(filename: str):
    path = static('json/' + filename)
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")
        

def update_points(data, priorities, choice, dependencies):
    points = 0
    for idx, i in enumerate(dependencies):
        prev_choice = data[str(i)]
        points += priorities[idx][prev_choice][choice]
        
    return points
     

def find_best_option(data, plan_data, priority_data, page):
    best_map = dict()
    if page > 1:
        for p in priority_data[str(page)]['dependencies']:
            for r in range(1,page):
                if data[str(r)] in p.keys():
                    for k, v in p[data[str(r)]].items():
                        if k in best_map:
                            best_map[k] += v
                        else:
                            best_map[k] = v
        
        max_val = max(best_map.values())
        best_map = {k:v for k, v in best_map.items() if v == max_val}
        best_option = next(iter(best_map))
    else:
        best_option = random.choice(['1A', '1B', '1C'])
    
    explanation = create_explanation(data, plan_data, best_option, page,
                                     priority_data[str(page)]["dependant"])
    
    return best_option, explanation
  

# def check_influence(best_map, data, priority_data, page):
#     if len(best_map) > 1 and priority_data[str(page)]["influence"]:
#         point_map = {}
#         for b in best_map:
#             point_map[b] = {}
#             for i in priority_data[str(page)]["influence"]:
#                 for idx, p in enumerate(priority_data[str(i)]["dependant"]):
#                     if str(p) in data:
#                         prev_dec = data[str(p)]
#                         if idx == 0:
#                             point_map[b] = priority_data[str(i)]["dependencies"][idx][prev_dec]
#                         elif p == page:
#                             for key in point_map[b].keys():
#                                 point_map[b][key] += priority_data[str(i)]["dependencies"][idx][prev_dec][key]
#                                 point_map[b][key] += priority_data[str(i)]["dependencies"][idx][b][key]
#                         else:
#                             for key in point_map[b].keys():
#                                 point_map[b][key] += priority_data[str(i)]["dependencies"][idx][prev_dec][key]
        
#         try:
#             max_val = 0
#             best_option = None
#             for key, inner_dict in point_map.items():
#                 inner_max = max(inner_dict.values())
#                 if inner_max > max_val:
#                     max_val = inner_max
#                     best_option = key
#         except:
#             best_option = max(best_map, key=best_map.get)
#     else:
#         best_option = max(best_map, key=best_map.get)
          
#     return best_option

def create_explanation(data, plan_data, best_option, page, dependencies):  
    if page == 1:
        for item in plan_data[str(page)]["items"]:
            if item["value"] == best_option:
                name = item["name"]
                characteristics = item["characteristics"]
                break
            
        explanation = "Als Ihr Berater empfehle ich Ihnen die Option '" + name + \
            "'. Diese Empfehlung besitzt die Eigenschaften " + characteristics + \
            ", welche ich als Vorteilhaft fuer unsere Firmengestaltung sehe."
    else:
        for item in plan_data[str(page)]["items"]:
            if item["value"] == best_option:
                name = item["name"]
                break

        explanation = "Als Ihr Berater empfehle ich Ihnen die Option '" + name + \
            "'. Meine Empfehlung beruht auf Ihrer Wahl "
        
        for idx, i in enumerate(dependencies):
            for item in plan_data[str(i)]["items"]:
                if item["value"] == data[str(i)]:
                    if idx == len(dependencies) - 1:
                        if len(dependencies) > 1:
                            explanation += "sowie '" + item["name"] + "'" + " bei Aufgabe " + str(i)
                        else:
                            explanation += "'" + item["name"] + "'" + " bei Aufgabe " + str(i)
                            break
                    else:
                        explanation += "'" + item["name"] + "'" + " bei Aufgabe " + str(i) + ", "
                        break
        
        if len(dependencies) > 1:
            explanation += ", deren jeweilige Eigenschaften "
        else:
            if dependencies != [2]:
                explanation += ", deren Eigenschaften "
            else: 
                explanation += "."
        
        for idx, i in enumerate(dependencies):
            for item in plan_data[str(i)]["items"]:
                if item["value"] == data[str(i)]:
                    if item["characteristics"]:
                        if len(dependencies) > 1:
                            if idx == len(dependencies) - 1:
                                explanation += "sowie " + item["characteristics"] + \
                                    " am besten zu unserem Konzept passen."
                                break
                            else:
                                explanation += item["characteristics"] + ", "
                                break
                        else:
                            explanation += item["characteristics"] + \
                                " am besten zu unserem Konzept passen."
    
    return explanation


def random_input_array():
    options = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    return random.choice(options)