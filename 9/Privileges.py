class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can delete account",
                           "can shut down server"]

    def show_privileges(self):
        print("Here is a list of admin privileges: ")
        for privilege in self.privileges:
            print(privilege.title())