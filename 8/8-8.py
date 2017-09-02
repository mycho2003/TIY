def make_album(name, title, tracks = 0):
    if tracks:
        return {"Name": name, "Title": title, "Tracks": tracks}
    else:
        return {"Name": name, "Title": title}
while True:
    iname = input("What is the artist's name?")
    ititle = input("What is the title of the album?")
    album = make_album(iname, ititle)
    print(album)
    quit = input("Would you like to quit?")
    if quit.title() == "Yes":
        break
