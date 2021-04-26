import unittest
from models.slot import Slot

# class Slot:

#     def __init__(self, slot_num, time_stamp, turbo_slot=None, id = None):
#       self.slot_num = slot_num
#       self.time_stamp = time_stamp
#       self.turbo_slot = turbo_slot
#       self.id = id

class TestSlot(unittest.TestCase):

    def setUp(self):
        self.slot_1 = Slot(1, "00:00-01:00", False)

    def test_slot_instance_variables_slot_num(self):
        self.assertEqual(1, self.slot_1.slot_num)

    def test_slot_instance_variables_time_stamp(self):
        self.assertEqual("00:00-01:00", self.slot_1.time_stamp)

    def test_slot_instance_variables_turbo_slot(self):
        self.assertEqual(False, self.slot_1.turbo_slot)