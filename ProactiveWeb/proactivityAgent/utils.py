import json

# file holds various utility functions for the app, such as calculating the points and creating the explanation


def read_json(path: str):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        return data
    except:
        print(f'Failed to read file {path}')


def write_json(path: str, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f)


def proactivity_encoding_to_text(proactivity):
    if proactivity == [1, 0, 0, 0]:
        return 'none'
    elif proactivity == [0, 1, 0, 0]:
        return 'notification'
    elif proactivity == [0, 0, 1, 0]:
        return 'suggestion'
    elif proactivity == [0, 0, 0, 1]:
        return 'intervention'


def proactivity_text_to_encoding(proactivity):
    if proactivity == 'none':
        return [1, 0, 0, 0]
    elif proactivity == 'notification':
        return [0, 1, 0, 0]
    elif proactivity == 'suggestion':
        return [0, 0, 1, 0]
    elif proactivity == 'intervention':
        return [0, 0, 0, 1]
