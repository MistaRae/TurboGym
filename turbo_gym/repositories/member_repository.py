from db.run_sql import run_sql
from models.member import Member


# CREATE TABLE members (
#     id SERIAL PRIMARY KEY, 
#     first_name VARCHAR(255),
#     Last_name VARCHAR(255),
#     age INT,
#     sex VARCHAR(255),
#     turbo_membership BOOLEAN,
#     active BOOLEAN
# );

def save(member):
    sql = "INSERT INTO memebers (first_name, last_name, age, sex, turbo_membership, active) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.Last_name, member.age, member.sex, member.turbo_membership, member.active]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member