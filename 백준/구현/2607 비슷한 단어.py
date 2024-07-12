n = int(input())
word = sorted(input())
res = 0

for _ in range(n-1):
  similar_word = sorted(input())
  same = 0
  start = 0

  for i in range(len(similar_word)):
    for j in range(start, len(word)):
      if similar_word[i] == word[j]:
        same += 1
        start = j+1
        break
  
  if len(similar_word) - same <= 1 and len(word) - same <= 1:
    res += 1

print(res)
