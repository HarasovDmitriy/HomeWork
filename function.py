#Импортируем библиотеки и класс
import json
from Class import Candidate

def load_candidates(filename):
    '''Загрузка кандидатов из файла'''
    with open('candidates.json', encoding='UTF-8') as file:
        data = json.load(file)
    return data

def get_all(data):
    '''Показать всех кондидатов'''
    arr = []
    for item in data:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        arr.append(candidate)
    return arr

def get_by_pk(pk, arr):
    '''Показать кондидата по его номеру'''
    for item in arr:
        if item.pk == pk:
            return item

def get_by_skill(skill_name, data):
    '''Показать кондидатов по их навыку'''
    arr = []
    for item in data:
        if skill_name in item.skills:
            arr.append(item)
        return arr

