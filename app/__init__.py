from flask import Flask

app = Flask(__name__)
# Используется для защиты данных (секретный ключ)
app.config['SECRET_KEY'] = 'never_forever'

from app import routes

