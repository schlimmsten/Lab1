# TODO решите задачу
import json

FILENAME = 'input.json'

def task() -> float:
    with open(FILENAME,'r') as file:
        json_obj = json.load(file)
        return round(sum(json_dict['score']*json_dict['weight'] for json_dict in json_obj),3)

print(task())
