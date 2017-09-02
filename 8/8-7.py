def make_album(name, title, tracks = 0):
    if tracks:
        return {"Name": name, "Title": title, "Tracks": tracks}
    else:
        return {"Name": name, "Title": title}
a = make_album("Me", "Em")
b = make_album("You", "Uoy")
c = make_album("Him", "Mih", 6)

print(a)
print(b)
print(c)