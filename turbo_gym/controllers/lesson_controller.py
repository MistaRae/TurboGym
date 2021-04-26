# imports go here 
from flask import Flask, render_template, redirect, request, Blueprint 
from models.lesson import Lesson 

import repositories.lesson_repository as lesson_repository
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
    lesson = lesson_repository.select(id)
    return render_template("lessons/index.html")
# NEW

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



    #   <!-- def __init__(self, class_name, class_type, difficulty, duration, capacity, slot_id = None, id=None):
    # self.class_name = class_name
    # self.class_type = class_type
    # self.difficulty = difficulty
    # self.duration = duration
    # self.capacity = capacity
    # self.slot_id = slot_id #time slot number references slot primary key
    # self.id = id  -->

# CREATE
# EDIT 
# UPDATE
# DELETE 