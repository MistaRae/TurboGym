from db.run_sql import run_sql
from models.slot import Slot



# CREATE TABLE slots (
#     id SERIAL PRIMARY KEY, 
#     slot_num INT,
#     time_stamp VARCHAR(255),
#     turbo_slot BOOLEAN
# );

def save(slot):
    sql = "INSERT INTO slots (slot_num, time_stamp, turbo_slot) VALUES (%s, %s, %s) RETURNING id"
    values = [slot.slot_num, slot.time_stamp, slot.turbo_slot]
    results = run_sql(sql, values)
    slot.id = results[0]['id']
    return slot
