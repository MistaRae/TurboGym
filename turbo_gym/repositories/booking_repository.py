from db.run_sql import run_sql
from models.booking import Booking



# CREATE TABLE bookings (
#     id SERIAL PRIMARY KEY,
#     member_id INT REFERENCES members(id),
#     lesson_id INT REFERENCES lessons(id)    
# );


def save(booking):
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) returning id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking