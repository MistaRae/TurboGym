from db.run_sql import run_sql
from models.lesson import Lesson 


# CREATE TABLE lessons (
#     id SERIAL PRIMARY KEY, 
#     name VARCHAR(255),
#     class_type VARCHAR(255),
#     difficulty VARCHAR(255),
#     duration INT,
#     capacity INT,
#     slot_id INT REFERENCES slots(id) ON DELETE CASCADE   
# );

def save(lesson):
    sql = "INSERT INTO lessons (name, class_type, difficulty, duration, capacity) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [lesson.name, lesson.class_type, lesson.difficulty, lesson.duration, lesson.capacity]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson