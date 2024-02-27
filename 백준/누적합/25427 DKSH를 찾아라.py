n = int(input())
string = input()
d = k = s = h = 0

for i in range(n):
    if string[i] == 'D':
        d += 1
    elif string[i] == 'K':
        k += d
    elif string[i] == 'S':
        s += k
    elif string[i] == 'H':
        h += s

print(h)
