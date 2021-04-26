from db.run_sql import run_sql
from models.slot import Slot



# CREATE TABLE slots (
#     id SERIAL PRIMARY KEY, 
#     slot_num INT,
#     time_stamp VARCHAR(255),
#     turbo_slot BOOLEAN
# );

# CREATE
def save(slot):
    sql = "INSERT INTO slots (slot_num, time_stamp, turbo_slot) VALUES (%s, %s, %s) RETURNING id"
    values = [slot.slot_num, slot.time_stamp, slot.turbo_slot]
    results = run_sql(sql, values)
    slot.id = results[0]['id']
    return slot

# READ 
def select(id):
    result = None
    sql = "SELECT * FROM slots WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        slot = Slot(result['slot_num'], result['time_stamp'], result['turbo_slot'], result['id'])
    return slot

def select_all():
    slots = []
    sql = "SELECT * FROM slots"
    results = run_sql(sql)

    for row in results:
        slot = Slot(row['slot_num'], row['time_stamp'], row['turbo_slot'], row['id'])
        slots.append(slot)
    return slots

# UPDATE 

def update(slot):
    sql = "UPDATE slots SET (slot_num, time_stamp, turbo_slot) = (%s, %s, %s) WHERE id = %s"
    values = [slot.slot_num, slot.time_stamp, slot.turbo_slot, slot.id]
    run_sql(sql, values)

# DELETE

def delete(id):
    sql = "DELETE * FROM slots WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM slots"
    run_sql(sql)