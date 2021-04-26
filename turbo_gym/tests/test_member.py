import unittest
from models.member import Member 

# class Member:

#     def __init__ (self, first_name, last_name, age, sex, turbo_membership=False, active=True, id=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.sex = sex
#         self.turbo_membership = turbo_membership
#         self.active = active
#         self.id = id

class TestMember(unittest.TestCase):

    def setUp(self):
        self.mark_rae = Member('Mark', 'Rae', 33, "male", True, True)
        self.sarah_burns = Member('Sarah', 'Burns', 28, "female", False, True)
        self.chris_rettie = Member('Chris', 'Rettie', 35, "male", True, True)
        self.jill_rettie = Member('jill', 'Rettie', 36, "female", False, True)   

    def test_member_instance_variables(self):
        self.assertEqual('Sarah', self.sarah_burns.first_name)
        self.assertEqual('Burns', self.sarah_burns.last_name)
        self.assertEqual(28, self.sarah_burns.age)
        self.assertEqual('female', self.sarah_burns.sex)
        self.assertEqual(False, self.sarah_burns.turbo_membership)
        self.assertEqual(True, self.sarah_burns.active)

    def test_member_full_name(self):
        self.assertEqual("Mark Rae", self.mark_rae.full_name(self.mark_rae))

    # def test_create_member(self):
    # unsure if i require this as the form should be feeding the controller with the user input 
    # then the member repository will feed the database. 

    def test_activate_turbo_membership(self):
        self.assertEqual(True, self.sarah_burns.activate_turbo_membership())
        
    def test_deactivate_turbo_membership(self):
        self.assertEqual(False, self.sarah_burns.deactivate_turbo_membership())

    def test_deactivate_membership(self):
        self.assertEqual(False, self.chris_rettie.deactivate_membership())

    def test_reactivate_membership(self):
        self.jill_rettie.deactivate_membership()
        self.assertEqual(True, self.jill_rettie.reactivate_membership())
