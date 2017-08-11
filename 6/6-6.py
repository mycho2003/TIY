favorite_languages = {"jen": "python", "sarah": "c", "phil": "python", "edward": "ruby"}
pollers = ["michael", "phil", "josh", "ben", "jen"]

for poller in pollers:
    if poller in favorite_languages:
        print("Thank you for responding to the poll, " + poller.title() + "!")
    else:
        print(poller.title() + ", you should take the poll!")
