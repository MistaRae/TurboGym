# imports go here 
from flask import Flask, render_template, redirect, request, Blueprint 
from models.lesson import Lesson 

import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository
import repositories.slot_repository as slot_repository

lessons_blueprint = Blueprint("lessons", __name__)

# INDEX
@lessons_blueprint.route("/classes")
def lessons():
    lessons = lesson_repository.select_all()
    slots = slot_repository.select_all()
    return render_template("lessons/index.html", lessons = lessons, slots = slots)

@lessons_blueprint.route('/classes/<id>')
def select_lesson(id):
    members = booking_repository.select_members_in_class(id)
    lesson = lesson_repository.select(id)
    slots = slot_repository.select_all()
    return render_template("lessons/lesson_info.html", lesson = lesson, slots = slots, members = members)

# NEW

@lessons_blueprint.route('/classes/new')
def new_lesson():
    slots = slot_repository.select_all()
    return render_template('lessons/new.html', slots = slots)

@lessons_blueprint.route('/classes', methods=['POST'])
def add_lesson():
    class_name = request.form["class_name"]
    class_type = request.form["class_type"]
    difficulty = request.form["difficulty"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    slot_id = request.form["slot_id"]
    lesson = Lesson(class_name, class_type, difficulty, duration, capacity, slot_id)
    lesson_repository.save(lesson)
    return redirect('/classes') 

# CREATE

# EDIT 
#gets form
@lessons_blueprint.route("/classes/<id>/update")
def edit_lesson(id):
    lesson = lesson_repository.select(id)
    slots = slot_repository.select_all()
    return render_template('lessons/update.html', lesson = lesson, slots = slots)

# UPDATE

#posts form, actions database
@lessons_blueprint.route('/classes/<id>', methods=['POST'])
def update_lesson(id):
    class_name = request.form['class_name']
    class_type = request.form['class_type']
    difficulty = request.form['difficulty']
    duration = request.form['duration']
    capacity = request.form['capacity']
    slot_id = request.form['slot_id']
    lesson = Lesson(class_name, class_type, difficulty, duration, capacity, slot_id, id)
    lesson_repository.update(lesson)
    return redirect('/classes')

# DELETE 



