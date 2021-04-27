from db.run_sql import run_sql
from models.lesson import Lesson 
from models.slot import Slot

# CREATE
def save(lesson):
    sql = "INSERT INTO lessons (class_name, class_type, difficulty, duration, capacity, slot_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [lesson.class_name, lesson.class_type, lesson.difficulty, lesson.duration, lesson.capacity, lesson.slot_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    lesson.id = id

# READ
def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        lesson = Lesson(result['class_name'], result['class_type'], result['difficulty'], result['duration'], result['capacity'], result['slot_id'], result['id'])
    return lesson

def select_all():
    lessons = []
    sql = "SELECT * FROM lessons"
    results = run_sql(sql)

    for row in results:
        lesson = Lesson(row['class_name'], row['class_type'], row['difficulty'], row['duration'], row['capacity'], row['slot_id'], row['id'])
        lessons.append(lesson)
    return lessons 

# UPDATE 

def update(lesson):
    sql = "UPDATE lessons SET (class_name, class_type, difficulty, duration, capacity, slot_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [lesson.class_name, lesson.class_type, lesson.difficulty, lesson.duration, lesson.capacity, lesson.slot_id, lesson.id]
    run_sql(sql, values)

# DELETE

def delete(id):
    sql = "DELETE * FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM lessons"
    run_sql(sql)