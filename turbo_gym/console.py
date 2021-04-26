# imports
import pdb
from models.slot import Slot
from models.member import Member
from models.lesson import Lesson 
from models.booking import Booking

import repositories.slot_repository as slot_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository

# repo imports 
# import repositories.slot_repository as slot_repository
# import repositories.member_repository as member_repository
# import repositories.lesson_repository as lesson_repository
# import repositories.booking_repository as booking_repository

# delete all tables

slot_repository.delete_all()
member_repository.delete_all()
lesson_repository.delete_all()

# pre-population/seeding goes here:

# CREATE TABLE slots (
#     id SERIAL PRIMARY KEY, 
#     slot_num INT,
#     time_stamp VARCHAR(255),
#     turbo_slot BOOLEAN
# );

slot_1 = Slot(1, "00:00-01:00", False)
slot_repository.save(slot_1)
slot_2 = Slot(2, "01:00-02:00", False)
slot_repository.save(slot_2)
slot_3 = Slot(3, "02:00-03:00", False)
slot_repository.save(slot_3)
slot_4 = Slot(4, "03:00-04:00", False)
slot_repository.save(slot_4)
slot_5 = Slot(5, "04:00-05:00", False)
slot_repository.save(slot_5)
slot_6 = Slot(6, "05:00-06:00", False)
slot_repository.save(slot_6)
slot_7 = Slot(7, "06:00-07:00", False)
slot_repository.save(slot_7)
slot_8 = Slot(8, "07:00-08:00", False)
slot_repository.save(slot_8)
slot_9 = Slot(9, "08:00-09:00", False)
slot_repository.save(slot_9)
slot_10 = Slot(10, "09:00-10:00", False)
slot_repository.save(slot_10)
slot_11 = Slot(11, "10:00-11:00", False)
slot_repository.save(slot_11)
slot_12 = Slot(12, "11:00-12:00", False)
slot_repository.save(slot_12)
slot_13 = Slot(13, "12:00-13:00", False)
slot_repository.save(slot_13)
slot_14 = Slot(14, "13:00-14:00", False)
slot_repository.save(slot_14)
slot_15 = Slot(15, "14:00-15:00", False)
slot_repository.save(slot_15)
slot_16 = Slot(16, "15:00-16:00", False)
slot_repository.save(slot_16)
slot_17 = Slot(17, "16:00-17:00", False)
slot_repository.save(slot_17)
slot_18 = Slot(18, "17:00-18:00", False)
slot_repository.save(slot_18)
slot_19 = Slot(19, "18:00-19:00", False)
slot_repository.save(slot_19)
slot_20 = Slot(20, "19:00-20:00", False)
slot_repository.save(slot_20)
slot_21 = Slot(21, "20:00-21:00", False)
slot_repository.save(slot_21)
slot_22 = Slot(22, "21:00-22:00", False)
slot_repository.save(slot_22)
slot_23 = Slot(23, "22:00-23:00", False)
slot_repository.save(slot_23)
slot_24 = Slot(24, "23:00-24:00", False)
slot_repository.save(slot_24)

#   class Member:

#  def __init__ (self, first_name, last_name, age, sex, turbo_membership=False, active=True, id=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.sex = sex
#         self.turbo_membership = turbo_membership
#         self.active = active
#         self.id = id

mark_rae = Member('Mark', 'Rae', 33, "male", True, True)
member_repository.save(mark_rae)
sarah_burns = Member('Sarah', 'Burns', 28, "female", False, True)
member_repository.save(sarah_burns)
chris_rettie = Member('Chris', 'Rettie', 35, "male", True, True)
member_repository.save(chris_rettie)
jill_rettie = Member('jill', 'Rettie', 36, "female", False, True)
member_repository.save(jill_rettie)

# class Lesson:

#     def __init__(self, class_name, class_type, difficulty, duration, capacity, slot_id = None, id=None):
#         self.class_name = class_name
#         self.class_type = class_type
#         self.difficulty = difficulty
#         self.duration = duration
#         self.capacity = capacity
#         self.slot_id = slot_id #time slot number references slot primary key
#         self.id = id 

beg_spin_class = Lesson("Spin Class", "cardio", "beginner", 55, 10, slot_10)
lesson_repository.save(beg_spin_class)
int_spin_class = Lesson("Spin Class", "cardio", "intermediate", 55, 10, slot_9)
lesson_repository.save(int_spin_class)
adv_spin_class = Lesson("Spin Class", "cardio", "advanced", 55, 10, slot_11)
lesson_repository.save(adv_spin_class)

test_booking = Booking(mark_rae, beg_spin_class)
booking_repository.save(test_booking)