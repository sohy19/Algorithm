N = input()
if len(N) == 1:   # N이 한 자리 수일 때 앞에 0을 붙여줌
    N = "0" + N
new_num = N
cycle = 0   # 사이클 길이

while True:
    cycle += 1
    k = int(new_num[0]) + int(new_num[1])   # 각 자리 수 합
    new_num = new_num[1] + str(k)[-1]   # 오른쪽 자리 수와 앞에서 구한 합의 오른쪽 자리 수를 이어 붙인 값
    if N == new_num:
        break
        
print(cycle)