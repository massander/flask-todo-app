from app import app, db
from flask import Flask, url_for, render_template, request, redirect
from datetime import date
import itertools
import json

from .models import Todo
from .forms import CreateForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classes/<group_id>')
def schedule(group_id):
    """return classes"""
    with open(r'data\classes.json', 'r', encoding='UTF-8') as jsonfile:
        try:
            load = json.load(jsonfile)
        except json.JSONDecodeError as er:
            print(er)
    if date(date.today().year,
            date.today().month,
            date.today().day).isocalendar()[1] % 2 == 0:
            return render_template('classes.html',
                                    group_id = group_id,
                                    load = load.get('classes').get(group_id).get('even'),
                                    rings = load.get('rings'))
    else:
        return render_template('classes.html',
                                group_id = group_id,
                                load = load.get('classes').get(group_id).get('odd'),
                                rings = load.get('rings'))

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return render_template('tasks.html', tasks=Todo.get_all())

@app.route('/tasks/create', methods=['GET', 'POST'])
def create_new_task():
    # if request.method == 'POST':
    #     new_task = Todo(subject=request.form['subject'],
    #                     content=request.form['content'],
    #                     deadline=request.form['deadline'])
    #     Todo.save_to_db(new_task)
    #     return redirect('/tasks')
    # else:
    #     return render_template('create.html')
    form = CreateForm()

    if form.validate_on_submit():
        new_task = Todo(form.subject.data, 
                        form.content.data, 
                        form.deadline.data)
        try:
            Todo.save_to_db(new_task)
            return redirect('/tasks')
        except:
            return 'There was an issue update that task'
    else:
        return render_template('create.html', form=form)


@app.route('/tasks/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    form = CreateForm()
    if form.validate_on_submit():
        new_task = Todo(form.subject.data, 
                        form.content.data, 
                        form.deadline.data)
        try:
            Todo.update_task()
            return redirect('/tasks')
        except:
            return 'There was an issue update that task'
    else:
        return render_template('update.html', form=form, task=task)

@app.route('/tasks/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        Todo.delete_task(task_to_delete)
        return redirect('/tasks')
    except:
        return "There was an issue deleting that task"

