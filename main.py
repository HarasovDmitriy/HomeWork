# Импортируем нужные библиотеку\функции
from flask import Flask
from function import get_all, load_candidates, get_by_pk, get_by_skill

#загружаем список кондидатов
FILENAME = 'candidates.json'
data = get_all(load_candidates(FILENAME))

#Странички
app = Flask(__name__)
@app.route('/')
def index():
    '''Стартовая страница'''
    str = "<pre>"
    for i in data:
        str += f'{i} \n \n'
    str += '</pre>'
    return str

@app.route('/candidates/<int:pk>')
def get_user(pk):
    '''Показывает информацию о кондидате по номеру'''
    user = get_by_pk(pk, data)
    if user:
        str = f'<img src = "{user.picture}">'
        str += f'<pre> {user} </pre>'
    else:
        str = "NOT FOUND"
    return str


@app.route('/skills/<x>')
def get_users(x):
    '''Показывает кондидатов по навыкам'''
    users = get_by_skill(x, data)
    if users:
        str = '<pre>'
        for i in users:
            str += f'{i} \n \n'
        str += '</pre>'
    else:
        str = 'NOT FOUND'
    return str

#Запускаем сайт на порту 5000
if __name__ == '__main__':
    app.run(port=5000)