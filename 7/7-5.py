while True:
    age = int(input("Please enter your age to see your ticket cost."))
    if age < 3:
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")