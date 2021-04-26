class Member:

    def __init__ (self, first_name, last_name, age, sex, turbo_membership=False, active=True, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.turbo_membership = turbo_membership
        self.active = active
        self.id = id

    def full_name(self, member):
        full_name = self.first_name + " " + self.last_name
        return full_name

    def create_member(self):
        pass

    def activate_turbo_membership(self):
        if self.turbo_membership is not True:
            self.turbo_membership = True
        return self.turbo_membership
        

    def deactivate_turbo_membership(self):
        if self.turbo_membership is not False:
            self.turbo_membership = False
        return self.turbo_membership

    def deactivate_membership(self):
        if self.active == True:
            self.active = False
        return self.active

    def reactivate_membership(self):
        if self.active == False:
            self.active = True 
        return self.active