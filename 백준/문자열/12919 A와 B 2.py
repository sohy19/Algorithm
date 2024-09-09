import sys
input = sys.stdin.readline

def making_string(string):  
  if len(string) == len(s):
    if string == s:
      return 1
    return 0
  
  if string[-1] == "A":   # 뒤 A가 있으면 A 제거
    if making_string(string[:len(string)-1]):
      return 1
  if string[0] == "B":   # 앞 B 있으면 제거 후 뒤집기
    if making_string("".join(reversed(string[1:]))):
      return 1
  
  return 0
  

s = input().strip()
t = input().strip()

print(making_string(t))
