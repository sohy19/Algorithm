most_name = ""
most_num = 0

for _ in range(7):
    name, num = input().split()
    if most_num < int(num):
        most_name = name
        most_num = int(num)

print(most_name)
