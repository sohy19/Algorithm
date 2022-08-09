import sys
input = sys.stdin.readline

n = int(input())   # 시험장의 개수
nums = list(map(int, input().split()))  # 각 시험장 내 응시자 수
first_sup, sec_sup = map(int, input().split())   #  총감독관이 감시할 수 있는 응시자 수, 부감독관이 감시할 수 있는 응시자 수

cnt = 0   # 필요한 감독관 최소 수

for num in nums:
  # 총감독관 감시
  num -= first_sup
  cnt += 1
  # 부감독관 감시
  if num > 0:
    if num % sec_sup == 0:
      cnt += (num // sec_sup)
    else:
      cnt += (num // sec_sup + 1)

print(cnt)
