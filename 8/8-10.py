def show_magicians(names):
    for name in names:
        print(name)


def make_great(names):
    for a in range(len(names)):
        name = names.pop(0) + " the Great"
        names.append(name)


magicnames = ["a", "b", "c"]
make_great(magicnames)
show_magicians(magicnames)