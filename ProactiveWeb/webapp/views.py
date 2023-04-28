import json

from django.shortcuts import redirect, render

from proactivityAgent.proactivity_agent import ProactivityAgent
from webapp.utils import (find_best_option, read_json, remove_json,
                          update_points, write_json)


def index(request):
    data = read_json('conversation.json') 
    context = {
        'data': data['index']
    }

    return render(request, 'index.html', context)


def personalData(request):
    if request.method == 'POST':
        form_data = dict(request.POST.items())
        form_data.pop("csrfmiddlewaretoken")
        
        proactivity_agent = ProactivityAgent()
        proactivity_agent.get_pers_data(form_data)
        print(proactivity_agent.pers_data)
        
        # json_data = json.dumps(form_data)            
        # write_json('personalData.json', json_data)
            
        return redirect('mainTask', page=1)
    
    data = read_json('conversation.json') 
    context = {
        'data': data['personalData']
    }
    
    return render(request, 'personalData.html', context)


def mainTask(request, page):
    proactivity_agent = ProactivityAgent()
    
    data = read_json('data.json')
    plan_data = read_json('databasePlanning.json')
    priorities = read_json('priorityPlanning.json')
        
    if request.method == 'POST':
        form_data = dict(request.POST.items())
        
        help_req = int(form_data['help_req_clicked'])
        sugg_req = int(form_data['sugg_req_clicked'])
        duration = float(form_data['duration'])
        
        form_data.pop("csrfmiddlewaretoken")
        form_data.pop("page")
        form_data.pop("help_req_clicked")
        form_data.pop("sugg_req_clicked")
        form_data.pop("duration")
            
        if page == 1 or data.get("points") is None:
            data = {}
            data["points"] = {}
            
        data.update(form_data)
        
        if page == 1:
            data["points"][str(page)] = 10
        else:
            data["points"][str(page)] = update_points(data, priorities[str(page)]["dependencies"], 
                                                    data[str(page)], priorities[str(page)]["dependant"])

        # TODO am ende mindestdauer pro seite auf 20s setzen und duration+20 mit duration ersetzen
        proactivity_agent.calc_data(page, help_req, sugg_req, duration+20, data["points"][str(page)])

        json_data = json.dumps(data)
        write_json('data.json', json_data)
        
        if page in [3,6,9,12]:
            return redirect('rate', page)
        else:
            page += 1
                
    if page > 12:
        return redirect('ending')
    
    input_array = proactivity_agent.return_proactivity(page)

    best_option, explanation = find_best_option(data, plan_data, priorities, page)
    
    for item in plan_data[str(page)]["items"]:
        if item["value"] == best_option:
            option_name = item["name"]
            option_path = item["path"]
            break

    context = {
        'data': plan_data[str(page)],
        'page_number': page,
        'best_option': best_option,
        'explanation': explanation,
        'input_array': input_array,
        'option_name': option_name,
        'option_path': option_path
    }
    
    return render(request, 'mainTask.html', context)
    
    
def rate(request, page):
    if request.method == 'POST':
        form_data = dict(request.POST.items())
        form_data.pop("csrfmiddlewaretoken")
        
        pers_data = read_json('personalData.json') 
        pers_data.update(form_data)
        pers_data = json.dumps(pers_data)            
        write_json('personalData.json', pers_data)
        
        return redirect('mainTask', page+1)
        
    conv_data = read_json('conversation.json')
    conv_data = conv_data['rate']
    plan_data = read_json('databasePlanning.json')
    data = read_json('data.json')
        
    task_data = []
    
    for i in conv_data[str(page)]["task_arr"]:        
        for item in plan_data[str(i)]["items"]:
            if item["value"] == data[str(i)]:
                path = item["path"]
                
        task_data.append({"points": data["points"][str(i)], "path": path, "task": i})
        
    points = sum(data["points"].values())
    max_points = conv_data[str(page)]["max_points"]
    points = f"{points} / {max_points}" 
    
    context = {
        'conv_data': conv_data, 
        'task_data': task_data,
        'points': points,
        'page_number': page,
        'task_arr': conv_data[str(page)]["task_arr"],
        'tasks': conv_data[str(page)]["tasks"],
        'check': conv_data[str(page)]["check"],
        'check_num': conv_data[str(page)]["check_num"],
    }
    
    return render(request, 'rate.html', context)
    
def ending(request):
    data = read_json('data.json')
    plan_data = read_json('databasePlanning.json')
    conv_data = read_json('conversation.json') 
    
    sum_points = sum(data["points"].values())
    
    contex_data = dict()        
    for i in plan_data:
        for item in plan_data[str(i)]["items"]:
            if item["value"] == data[str(i)]:
                if contex_data.get(str(i)) is None:
                    contex_data[str(i)] = {}
                contex_data[str(i)]["path"] = item["path"]
                contex_data[str(i)]["points"] = data["points"][str(i)]
                contex_data[str(i)]["title"] = plan_data[str(i)]["title"].split(": ")[1].strip()
                break
        
    remove_json("data.json")
    remove_json("personalData.json")
    
    context = {
        'contex_data': contex_data,
        'sum_points': sum_points,
        'conv_data': conv_data["ending"],
    }
    return render(request, "ending.html", context)
