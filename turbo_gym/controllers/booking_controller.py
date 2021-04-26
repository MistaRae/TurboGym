# imports go here 
from flask import Flask, render_template, redirect, request, Blueprint 
from models.booking import Booking 

import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)
# NEW
# CREATE
# EDIT 
# UPDATE
# DELETE 