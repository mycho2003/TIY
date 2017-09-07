class User:
    def __init__(self, first_name, last_name, picture, content):
        self.firstname = first_name
        self.lastname = last_name
        self.picture = picture
        self.content = content

    def describe_user(self):
        print(self.firstname.title() + " " + self.lastname.title() + "'s profile picture is " + self.picture +
              ". On this website, their content is: " + self.content)

    def greet_user(self):
        print("Hi " + self.firstname.title() + " " + self.lastname.title() + ", how are you doing today?")

Me = User("Michael", "Cho", "a dragon", "Multiple youtube videos and a music playlist")
You = User("Someone", "Else", "a meme", "absolutely nothing you care about")

Me.describe_user()
You.describe_user()