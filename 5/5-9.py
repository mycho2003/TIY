username = []

if username:
    for un in username:
        if un == "admin":
            print("Hello admin, the server is in critical condition!")
        else:
            print("Welcome, " + un + "!")
else:
    print("We need to find some users!")