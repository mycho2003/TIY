class User:
    def __init__(self, first_name, last_name, picture, content):
        self.firstname = first_name
        self.lastname = last_name
        self.picture = picture
        self.content = content
        self.login_attempts = 0

    def describe_user(self):
        print(self.firstname.title() + " " + self.lastname.title() + "'s profile picture is " + self.picture +
              ". On this website, their content is: " + self.content)

    def greet_user(self):
        print("Hi " + self.firstname.title() + " " + self.lastname.title() + ", how are you doing today?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0