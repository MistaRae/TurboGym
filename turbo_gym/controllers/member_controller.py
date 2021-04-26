# imports go here 
from flask import Flask, render_template, redirect, request, Blueprint 
from models.booking import Booking 
from models.member import Member

import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route('/members/<id>')
def my_classes(id):
    member = member_repository.select(id)
    lessons = member_repository.lessons(member)
    return render_template('members/my_classes.html', member = member, lessons = lessons)

@members_blueprint.route('/members/my-classes/<lesson_id>')
def class_info(lesson_id):
    lesson = lesson_repository.select(lesson_id)
    return render_template('/members/class_info.html', lesson = lesson)

# NEW
# CREATE
@members_blueprint.route('/members/new', methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    sex = request.form['sex']
    member = Member(first_name, last_name, age, sex)
    member_repository.save(member)
    return render_template('members/new.html', member = member)


# EDIT 
# UPDATE


# DELETE 
@members_blueprint.route('/members/my-classes/<lesson_id>/delete', methods=['POST'])
def cancel_booking(lesson_id):
    lesson_repository.delete(lesson_id)
    return redirect('/members')

