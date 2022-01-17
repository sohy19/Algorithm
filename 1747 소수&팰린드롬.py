import sys, math

N = sys.stdin.readline
num = int(N)-1   # 소수이면서 팰린드롬인 수

def prime_num(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def palindrome(num):
    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            return False
    return True

while True:
    num += 1
    if not prime_num(num):   # 소수 판별
        continue
    if not palindrome(str(num)):   # 팰린드롬 판별
        continue
    break

print(num)
