import unittest
from models.lesson import Lesson 
from models.slot import Slot

# class Lesson:

#     def __init__(self, class_name, class_type, difficulty, duration, capacity, slot_id = None, id=None):
#         self.class_name = class_name
#         self.class_type = class_type
#         self.difficulty = difficulty
#         self.duration = duration
#         self.capacity = capacity
#         self.slot_id = slot_id #time slot number references slot primary key
#         self.id = id 

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.slot_9 = Slot(9, "08:00-09:00", False)
        self.slot_10 = Slot(10, "09:00-10:00", False)
        self.slot_11 = Slot(11, "10:00-11:00", False)
        self.beg_spin_class = Lesson("Spin Class", "cardio", "beginner", 55, 10, self.slot_10)
        self.int_spin_class = Lesson("Spin Class", "cardio", "intermediate", 55, 10, self.slot_9)
        self.adv_spin_class = Lesson("Spin Class", "cardio", "advanced", 55, 10, self.slot_11)

    def test_lesson_instance_variables(self):
        self.assertEqual("Spin Class", self.beg_spin_class.class_name)
        self.assertEqual("cardio", self.beg_spin_class.class_type)
        self.assertEqual("beginner", self.beg_spin_class.difficulty)
        self.assertEqual(55, self.beg_spin_class.duration)
        self.assertEqual(10, self.beg_spin_class.capacity)
        self.assertEqual(self.slot_10, self.beg_spin_class.slot_id)


    # ALL OF THESE ARE REPO FUNCTIONS
    # def create_lesson(self):
    #     pass

    # def display_lesson(self):
    #     pass

    # def display_all_lessons(self):
    #     pass

    