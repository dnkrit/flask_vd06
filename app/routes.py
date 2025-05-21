from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
# Извлекает значения из title и content с проверкой наполенния полей
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)

@app.route('/anketa', methods=['GET', 'POST'])
def anketa():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        return render_template('anketa.html', submitted=True, name=name, city=city, hobby=hobby, age=age)
    return render_template('anketa.html', submitted=False)
