Gist = ["Bob", "Joe", "Billy"]
for g in Gist:
    print("Hi " + g + ", come over for dinner sometime")
print("\nBut wait, Joe can't come!\n")
del Gist[1]
Gist.insert(1, "BillyBob")
for g in Gist:
    print("Hi " + g + ", can you come over for dinner tonight?")
print("\nWait, I found a larger dinner table! I'll invite more people.\n")
Gist.insert(0, "Napoleon")
Gist.insert(2, "Caesar")
Gist.append("Trump")
for g in Gist:
    print("For the last time, " + g + ", can you come over for dinner?")
print("\nBut the table didn't arrive, so sorry, only 2 people can come.\n")
Gist.pop()
Gist.pop()
Gist.pop()
Gist.pop()
for g in Gist:
    print("Hey " + g + ", I choose you!")
print("In the end, I invite", len(Gist))

