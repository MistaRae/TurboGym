# imports go here 
from flask import Flask, render_template, redirect, request, Blueprint 
from models.booking import Booking 
from models.member import Member

import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
import repositories.slot_repository as slot_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
# shows all gym members
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

# shows all lessons that gym member has signed up to
@members_blueprint.route('/members/<id>')
def my_classes(id):
    member = member_repository.select(id)
    lessons = member_repository.lessons(member)
    return render_template('members/my_classes.html', member = member, lessons = lessons)

# shows all information on the selected lesson
@members_blueprint.route('/members/my-classes/<lesson_id>')
def class_info(lesson_id):
    lesson = lesson_repository.select(lesson_id)
    slots = slot_repository.select_all()
    return render_template('/members/class_info.html', lesson = lesson, slots = slots)

# NEW
# gets form for new member 
@members_blueprint.route('/members/new', methods=['GET'])
def new_member():
    members = member_repository.select_all()
    return render_template('members/new.html', members = members)

# CREATE
# processes form for new user on submission 
@members_blueprint.route('/members', methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    sex = request.form['sex']
    member = Member(first_name, last_name, age, sex)
    member_repository.save(member)
    return redirect('/members')


# EDIT 
#  gets form for amending/updating user details
@members_blueprint.route('/members/<id>/edit')
def edit_member(id):
    member = member_repository.select(id)
    lessons = member_repository.lessons(member)
    return render_template('members/update.html', member = member, lessons = lessons)
    

# UPDATE
# processes form for amended/updated user details and updates database entry
@members_blueprint.route('/members/<id>', methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    sex = request.form['sex']
    member = Member(first_name, last_name, age, sex, id=id)
    member_repository.update(member)
    return redirect('/members')

# QUIT GYM
# sets member's membership to inactive (active = False) and updates the entry in the database
@members_blueprint.route('/members/<id>/deactivate', methods=['POST'])
def deactivate_member(id):
    member = member_repository.select(id)
    member.deactivate_membership()
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route('/members/<id>/reactivate', methods = ['POST'])
def reactivate_member(id):
    member = member_repository.select(id)
    member.reactivate_membership()
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route('/members/<id>/turbo', methods = ['POST'])
def activate_turbo(id):
    member = member_repository.select(id)
    member.activate_turbo_membership()
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route('/members/<id>/deactivate-turbo', methods = ['POST'])
def deactivate_turbo(id):
    member = member_repository.select(id)
    member.deactivate_turbo_membership()
    member_repository.update(member)
    return redirect('/members')
