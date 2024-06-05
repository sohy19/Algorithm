import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  teams = list(map(int, input().split()))
  counter = Counter(teams)
  scores = {}

  rank = 1
  for i in range(N):
    if counter[teams[i]] == 6:
      if teams[i] in scores:
        scores[teams[i]].append(rank)
      else:
        scores[teams[i]] = [rank]
      rank += 1
  
  print(sorted(scores, key = lambda x:(sum(scores[x][0:4]), scores[x][4]))[0])
