string = input()
i = 0

for i in range(len(string)):
    if not i == 0 and i % 10 == 0:
        print()
    print(string[i], end='')
