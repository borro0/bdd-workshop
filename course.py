# This is your production code, all business logic should go here
class Course:
    def __init__(self):
        self.registrations = 0
        self.names = []
        self.maximum = 0

    def register(self, name):
        self.registrations += 1
