import json
from Class import Candidate

#которая загрузит данные из файла



def load_candidates(filename):
    with open('candidates.json', encoding='UTF-8') as file:
        data = json.load(file)
    return data

#которая покажет всех кандидатов
def get_all(data):
    arr = []
    for item in data:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        arr.append(candidate)
    return arr

#которая вернет кандидата по pk
def get_by_pk(pk, arr):
    for item in arr:
        if item.pk == pk:
            return item


#которая вернет кандидатов по навыку
def get_by_skill(skill_name, data):
    arr = []
    for item in data:
        if skill_name in item.skills:
            arr.append(item)
        return arr

