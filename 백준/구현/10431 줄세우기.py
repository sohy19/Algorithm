P = int(input())

for _ in range(P):
    height = list(map(int, input().split()))
    step = 0
    for i in range(2, 21):
        for j in range(1, i):
            if height[i] < height[j]:
                step += (i - j)
                height.insert(j, height.pop(i))
                break
    
    print(height[0], step)
