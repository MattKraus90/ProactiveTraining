import hashlib
import uuid

from django.shortcuts import redirect, render
from proactivityAgent.proactivity_agent import ProactivityAgent
from webapp.utils import (find_best_option, random_strategy, read_json,
                          remove_json, update_points, write_json)


def index(request):
    stragedy = random_strategy()
    request.session['user_hash'] = hashlib.sha256(
        str(uuid.uuid4()).encode()).hexdigest()
    request.session['stragedy'] = stragedy

    conv_data = read_json('conversation.json')
    context = {
        'data': conv_data['index']
    }

    return render(request, 'index.html', context)


def personalData(request):
    user_hash = request.session.get('user_hash')
    stragedy = request.session.get('stragedy')

    if request.method == 'POST':
        form_data = dict(request.POST.items())
        form_data.pop("csrfmiddlewaretoken")
        data = {}
        data['personalData'] = form_data
        data['strategy'] = stragedy
        write_json(f"data_{user_hash}.json", data)

        proactivity_agent = ProactivityAgent(user_hash, stragedy)
        proactivity_agent.get_pers_data(form_data)
        print(proactivity_agent.pers_data)

        return redirect('mainTask', page=1)

    data = read_json('conversation.json')
    context = {
        'headline': data['personalData']['headline'],
        'text': data['personalData']['text'],
        'user_id': data['personalData']['user_id'],
        'gender': data['personalData']['gender'],
        'age': data['personalData']['age'],
        'TA_text': data['personalData']['TA_text'],
        'TA': data['personalData']['TA'],
        'PreTrust_text': data['personalData']['PreTrust_text'],
        'PreTrust': data['personalData']['PreTrust'],
        'Personality_text': data['personalData']['Personality_text'],
        'Personality': data['personalData']['Personality'],
        'ExperienceEco_text': data['personalData']['ExperienceEco_text'],
        'ExperienceEco': data['personalData']['ExperienceEco'],
        'notice': data['personalData']['notice'],
    }

    return render(request, 'personalData.html', context)


def mainTask(request, page):
    user_hash = request.session.get('user_hash')
    stragedy = request.session.get('stragedy')
    proactivity_agent = ProactivityAgent(user_hash, stragedy)

    data = read_json(f"data_{user_hash}.json")
    plan_data = read_json("databasePlanning.json")
    priorities = read_json("priorityPlanning.json")

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

        if page == 1:
            data['mainTask'] = {}
            data['mainTask']['points'] = {}

        data['mainTask'].update(form_data)

        if page == 1:
            data['mainTask']['points'][str(page)] = 10
        else:
            data['mainTask']['points'][str(page)] = update_points(data, priorities[str(
                page)]['dependencies'], data['mainTask'][str(page)], priorities[str(page)]['dependant'])

        # TODO am ende mindestdauer pro seite auf 20s setzen und duration+20 mit duration ersetzen
        proactivity_agent.calc_data(
            page, help_req, sugg_req, duration+20, data['mainTask']['points'][str(page)])

        write_json(f"data_{user_hash}.json", data)

        if page in [3, 6, 9, 12]:
            return redirect('rate', page)
        else:
            page += 1

    if page > 12:
        return redirect('ending')

    input_array = proactivity_agent.return_proactivity(page)

    best_option, explanation = find_best_option(
        data, plan_data, priorities, page)

    for item in plan_data[str(page)]['items']:
        if item['value'] == best_option:
            option_name = item['name']
            option_path = item['path']
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
    user_hash = request.session.get('user_hash')
    data = read_json(f"data_{user_hash}.json")

    if request.method == 'POST':
        form_data = dict(request.POST.items())
        form_data.pop("csrfmiddlewaretoken")

        data['rate'] = {}
        data['rate'][str(page)] = {}
        data['rate'][str(page)].update(form_data)
        write_json(f"data_{user_hash}.json", data)

        return redirect('mainTask', page+1)

    conv_data = read_json("conversation.json")
    conv_data = conv_data['rate']
    plan_data = read_json("databasePlanning.json")

    task_data = []

    for i in conv_data[str(page)]['task_arr']:
        for item in plan_data[str(i)]['items']:
            if item['value'] == data['mainTask'][str(i)]:
                path = item['path']

        task_data.append(
            {'points': data['mainTask']['points'][str(i)], 'path': path, 'task': i})

    points = sum(data['mainTask']['points'].values())
    max_points = conv_data[str(page)]['max_points']
    points = f"{points} / {max_points}"

    context = {
        'conv_data': conv_data,
        'task_data': task_data,
        'points': points,
        'page_number': page,
        'task_arr': conv_data[str(page)]['task_arr'],
        'tasks': conv_data[str(page)]['tasks'],
        'check': conv_data[str(page)]['check'],
        'check_num': conv_data[str(page)]['check_num'],
    }

    return render(request, 'rate.html', context)


def ending(request):
    user_hash = request.session.get('user_hash')
    stragedy = request.session.get('stragedy')
    proactivity_agent = ProactivityAgent(user_hash, stragedy)

    data = read_json(f"data_{user_hash}.json")
    plan_data = read_json("databasePlanning.json")
    conv_data = read_json("conversation.json")

    sum_points = sum(data['mainTask']['points'].values())

    contex_data = dict()
    for i in plan_data:
        for item in plan_data[str(i)]['items']:
            if item['value'] == data['mainTask'][str(i)]:
                if contex_data.get(str(i)) is None:
                    contex_data[str(i)] = {}
                contex_data[str(i)]['path'] = item['path']
                contex_data[str(
                    i)]['points'] = data['mainTask']['points'][str(i)]
                contex_data[str(i)]['title'] = plan_data[str(i)
                                                         ]['title'].split(": ")[1].strip()
                break

    user_data = read_json("user_data.json")
    if user_data is None:
        user_data = {}
    index = len(user_data)
    user_data[index] = data

    write_json("user_data.json", user_data)
    remove_json(f"data_{user_hash}.json")
    proactivity_agent.remove_instance(user_hash)

    context = {
        'contex_data': contex_data,
        'sum_points': sum_points,
        'conv_data': conv_data['ending'],
    }
    return render(request, 'ending.html', context)
