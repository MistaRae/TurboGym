# imports go here 
from flask import Flask, render_template, redirect, request, Blueprint 
from models.booking import Booking 

import repositories.booking_repository as booking_repository
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository
import repositories.slot_repository as slot_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)
# NEW

@bookings_blueprint.route('/classes/bookings/<lesson_id>', methods= ['POST']) 
def new_booking(lesson_id):
    slots = slot_repository.select_all()
    lesson = lesson_repository.select(lesson_id)
    members = member_repository.select_all()
    return render_template('/bookings/new.html', lesson = lesson, members = members, slots = slots)

@bookings_blueprint.route('/bookings/new', methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    lesson_id = request.form['lesson_id']
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    booking = Booking(member, lesson)
    booking_repository.save(booking)
    return redirect('/bookings')

@bookings_blueprint.route('/bookings/<id>/cancel', methods=['POST'])
def cancel_booking(id):
    booking_repository.delete(id)
    return redirect('/bookings')


# CREATE
# EDIT 
# UPDATE
# DELETE
