from db.run_sql import run_sql
from models.booking import Booking
from models.slot import Slot
from models.member import Member

import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
# CREATE TABLE bookings (
#     id SERIAL PRIMARY KEY,
#     member_id INT REFERENCES members(id),
#     lesson_id INT REFERENCES lessons(id)    
# );

# CREATE 
def save(booking):
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

# READ
def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        booking = Booking(result['member_id'], result['lesson_id'], result['id'])
    return booking
    

# READ
def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        lesson = lesson_repository.select(row['lesson_id'])
        booking = Booking(member, lesson, row['id'])
        bookings.append(booking)
    return bookings

def select_members_in_class(lesson):
    members = []
    sql = "SELECT members.* FROM bookings INNER JOIN members ON bookings.member_id = members.id WHERE bookings.lesson_id = %s"
    values = [lesson]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row['first_name'], row['last_name'],row['age'], row['sex'], row['turbo_membership'], row['active'], row['id'])
        members.append(member)
    return members
 


# SQL FOR MEMBERS BOOKED ONTO CLASS:
# SELECT members.* 
# FROM bookings 
# INNER JOIN members 
# ON bookings.member_id = members.id 
# WHERE member_id = 69

# SELECT lessons.* 
# FROM bookings 
# INNER JOIN lessons 
# ON bookings.lesson_id = lessons.id 
# WHERE bookings.member_id = 69


# def lesson_time(lesson):
#     result = None
#     sql = "SELECT slots.* FROM slots INNER JOIN lessons ON lessons.slots_id = slots.id WHERE id = %s"
#     values = [lesson.id]
#     result = run_sql(sql, values)
#     if result is not None:
#         slot = Slot(slot_num, time_stamp, turbo_slot,)


#UPDATE
def update(booking):
    sql = "UPDATE bookings SET (member_id, lesson_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.lesson.id, booking.id]
    run_sql(sql,values)

# DELETE
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

# DELETE
def delete_all():
    sql = "DELETE * FROM bookings"
    run_sql(sql)

