char = input()

for c in char:
    if c.islower():
        print(c.upper(), end="")
    else:
        print(c.lower(), end="")
