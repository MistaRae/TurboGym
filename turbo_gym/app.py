# imports

from flask import Flask
from flask import render_template
# import blueprints

# from controllers.booking_controller import bookings_blueprint
# from controllers.lesson_controller import lessons_blueprint
# from controllers.member_controller import members_blueprint
# from controllers.slot_controller import slots_blueprint

app = Flask(__name__)

# register blueprints

# app.register_blueprint(bookings_blueprint)
# app.register_blueprint(lessons_blueprint)
# app.register_blueprint(members_blueprint)
# app.register_blueprint(slots_blueprint)

@app.route("/")
def main():
    return render_template("index.html",)

if __name__ == '__main__':
    app.run(debug=True)
