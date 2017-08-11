current_users = ["chrimicho", "mycho2003", "hayaboy", "hellobye", "pycharm"]
new_users = ["admin", "ramaster", "mYchO2003", "IDLE", "tRuMp"]

counter = 0

for user in new_users:
    for us in current_users:
        if user.lower() == us.lower():
            print("This username has already been taken, please enter a new username.")
        else:
            counter += 1
    if counter == len(current_users):
        print("This username is available.")
    counter = 0