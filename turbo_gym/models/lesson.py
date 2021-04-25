class Lesson:

    def __init__(self, class_name, class_type, difficulty, duration, capacity, slot_id = None, id=None):
        self.class_name = class_name
        self.class_type = class_type
        self.difficulty = difficulty
        self.duration = duration
        self.capacity = capacity
        self.slot_id = slot_id #time slot number references slot primary key
        self.id = id 

# do i need an empty list to store the lesson occupants? 

    def create_lesson(self):
        pass

    def display_lesson(self):
        pass

    def display_all_lessons(self):
        pass
