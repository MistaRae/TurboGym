# imports go here 
from flask import Flask, render_template, redirect, request, Blueprint 
from models.lesson import Lesson 

import repositories.lesson_repository as lesson_repository

lessons_blueprint = Blueprint("lessons", __name__)

# INDEX
@lessons_blueprint.route("/classes")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.html", lessons = lessons)


# NEW


# CREATE
# EDIT 
# UPDATE
# DELETE 