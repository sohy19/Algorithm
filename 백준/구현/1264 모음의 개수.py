while True:
    char = input()
    num = 0
    if char == '#':
        break
    for c in char:
        if c.lower() in ('a', 'e', 'i', 'o', 'u'):
            num += 1
    print(num)
