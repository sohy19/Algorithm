import sys
input = sys.stdin.readline

n, m = map(int, input().split())   # n: 단어 개수, m: 외울 단어 길이 기준

words_cnt = {}
for _ in range(n):
  word = input().strip()
  if len(word) >= m:
    if word in words_cnt:
      words_cnt[word] += 1
    else:
      words_cnt[word] = 1

words = []
for key, value in words_cnt.items():
  words.append((key, value))

words.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for word in words:
  print(word[0])
