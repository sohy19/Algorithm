string = input()
cnt = 0

for s in string:
    if s in ('a', 'e', 'i', 'o', 'u'):
        cnt += 1

print(cnt)
