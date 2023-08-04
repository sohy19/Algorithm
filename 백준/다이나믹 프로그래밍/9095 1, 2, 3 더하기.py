T = int(input())    # 테스트 케이스 개수
N = []  # 정수 n 저장

for i in range(T):
    N.append(int(input()))

C = [0 for i in range(max(N)+1)]  # n을 1, 2, 3의 합으로 나타내는 방법의 수

for i in range(1, max(N)+1):
    if i == 1:
        C[i] = 1
    elif i == 2:
        C[i] = 2
    elif i == 3:
        C[i] = 4
    else:
        C[i] = C[i-1] + C[i-2] + C[i-3]

for i in range(T):
    print(C[N[i]])
