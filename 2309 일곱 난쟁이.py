import sys
input = sys.stdin.readline

def finding_seven():
    for i in range(9):
        elmt1 = dwaf.pop(i)
        for j in range(i, 8):
            elmt2 = dwaf.pop(j)
            if sum(dwaf) == 100:
                return
            else:
                dwaf.insert(j, elmt2)
        dwaf.insert(i, elmt1)

dwaf = []
for _ in range(9):
    dwaf.append(int(input()))

finding_seven()
dwaf.sort()
for i in range(7):
    print(dwaf[i])