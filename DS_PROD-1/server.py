from flask import Flask, request, jsonify
import datetime
import numpy as np
from joblib import load

# Загрузка модели
model = load('DS_PROD-1\model.pkl')

# Создание Flask-приложения
app = Flask(__name__)

# Создание эндпоинта для приема POST-запросов
@app.route("/predict", methods=["POST"])
def predict():
    # Извлечение признаков из запроса
    features = request.json

    # Преобразование входных данных в numpy-массив
    features = np.array(features).reshape(1, 4)

    # Получение предсказания модели
    prediction = model.predict(features)[0]

    # Возвращение ответа в формате JSON
    return jsonify({"prediction": prediction})


@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello, {name}!'


@app.route('/')
def index():
    return "Test message. The server is running"


@app.route('/time')
def cur_time():
    now = datetime.datetime.now()
    return str(now) 

@app.route('/add', methods=['POST'])
def add():
    num = request.json.get('num')
    if num > 10:
        return 'too much', 400
    return jsonify({'result': num + 1})


if __name__ == '__main__':
    app.run('localhost', 5000)