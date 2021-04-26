from flask import Flask, render_template, redirect, request, Blueprint
from models.slot import Slot

import repositories.slot_repository as slot_repository

slots_blueprint = Blueprint("slots", __name__)

# INDEX
@slots_blueprint.route("/slots")
def slots():
    slots = slot_repository.select_all()
    return render_template("slots/index.html", slots = slots)
# NEW
# CREATE
# EDIT 
# UPDATE
# DELETE 