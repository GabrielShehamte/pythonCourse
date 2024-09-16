from flask import Flask, render_template, request, redirect, url_for
from functions import get_todos, write_todos
app = Flask(__name__)

# @app.route('/')
def index():
    todos = get_todos()
    todos = [todos.strip() for todo in todos]
    return render_template('index.html', todos = todos)

# @app.route('/add', methods = ['POST'])
def add_todo():
    todo = request.form.get('todo') + "\n"
    todos = get_todos()
    todos.append(todo)
    write_todos(todos)
    return redirect(url_for('index'))

# @app.route('/update/<int:index>',methods = ['POST'])
def update_todo():
    new_todo = request.form.get('todo') + "\n"
    todos = get_todos()
    if 0<= index < len(todos):
        todos[index] = new_todo
        write_todos(todos)
    return redirect(url_for('index'))

# @app.route('/complete/<int:index>')
def complete_todo(index):
    todos = get_todos()
    if 0 <= index < len(todos):
        todos.pop(index)
        write_todos(todos)
    return redirect(url_for('index'))
