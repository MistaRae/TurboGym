from db.run_sql import run_sql
from models.booking import Booking



# CREATE TABLE bookings (
#     id SERIAL PRIMARY KEY,
#     member_id INT REFERENCES members(id),
#     lesson_id INT REFERENCES lessons(id)    
# );

# CREATE 
def save(booking):
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) returning id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

# READ
def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if booking is not None:
        booking = Booking(result['member_id'], result['lesson_id'], result['id'])
    return booking
    

# READ
def select_all():
    bookings = []
    sql = "SELECT * FROM bookings WHERE"
    result = run_sql(sql)

    for row in bookings:
        booking = Booking(row['member_id'], row['lesson_id'], row['id'])
        bookings.append(booking)
    return bookings

#UPDATE
def update(booking):
    sql = "UPDATE bookings SET (member_id, lesson_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.lesson.id, booking.id]
    run_sql(sql,values)

# DELETE
def delete(id):
    sql = "DELETE * FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

# DELETE
def delete_all():
    sql = "DELETE * FROM bookings"
    run_sql(sql)
