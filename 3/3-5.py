Gist = ["Bob", "Joe", "Billy"]
for g in Gist:
    print("Hi " + g + ", come over for dinner sometime")
print("But wait, Joe can't come!")
del Gist[1]
Gist.insert(1, "BillyBob")
for g in Gist:
    print("Hi " + g + ", can you come over for dinner tonight?")
