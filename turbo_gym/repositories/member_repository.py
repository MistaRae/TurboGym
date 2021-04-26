from db.run_sql import run_sql
from models.member import Member
from models.lesson import Lesson


# CREATE TABLE members (
#     id SERIAL PRIMARY KEY, 
#     first_name VARCHAR(255),
#     Last_name VARCHAR(255),
#     age INT,
#     sex VARCHAR(255),
#     turbo_membership BOOLEAN,
#     active BOOLEAN
# );

# CREATE
def save(member):
    sql = "INSERT INTO members (first_name, last_name, age, sex, turbo_membership, active) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.age, member.sex, member.turbo_membership, member.active]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

# READ 

def select(id):
    member = None 
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'],result['age'], result['sex'], result['turbo_membership'], result['active'], result['id'])
    return member

def select_all():
    members = [] 
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'],row['age'], row['sex'], row['turbo_membership'], row['active'], row['id'])
        members.append(member)
    return members

# UPDATE
def update(member):
    sql = "UPDATE members SET (first_name, last_name, age, sex, turbo_membership, active) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.Last_name, member.age, member.sex, member.turbo_membership, member.active, member.id]
    run_sql(sql, values)

# DELETE

def delete(id):
    sql = "DELETE * FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def lessons(member):
    bookings = []
    sql = "SELECT lessons.* FROM lessons INNER JOIN bookings ON bookings.lesson_id = lessons.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql,values)

    for row in results:
        lesson = Lesson(row['class_name'], row['class_type'], row['difficulty'], row['duration'], row['capacity'], row['slot_id'], row['id'])
        bookings.append(lesson)
    return bookings

def quit(member):
    member.deactivate_membership()
    sql = "UPDATE members SET (active) to (%s) WHERE id = %s"
    values = (member.active, member.id)
    run_sql(sql, values)