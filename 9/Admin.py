from User import User
from Privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, picture, content):
        super().__init__(first_name, last_name, picture, content)
        self.privileges = Privileges()