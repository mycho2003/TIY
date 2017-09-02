def show_magicians(names):
    for name in names:
        print(name)


def make_great(names):
    great = []
    for a in range(len(names)):
        name = names.pop(0)
        great.append(name + " the Great")
        names.append(name)
    return great


magicnames = ["a", "b", "c"]
magicians = make_great(magicnames)
show_magicians(magicnames)
show_magicians(magicians)