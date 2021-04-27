# imports go here 
from flask import Flask, render_template, redirect, request, Blueprint 
from models.booking import Booking 

import repositories.booking_repository as booking_repository
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)
# NEW

@bookings_blueprint.route('/classes/bookings/<lesson_id>', methods= ['POST']) 
def new_booking(lesson_id):
    lesson = lesson_repository.select(lesson_id)
    members = member_repository.select_all()
    return render_template('/bookings/new.html', lesson = lesson, members = members)

# @bookings_blueprint.route('/bookings/new')
    

# @bookings_blueprint.route('/bookings/new')
# def create_booking():
#     member_id = request.form()



# CREATE
# EDIT 
# UPDATE
# DELETE
