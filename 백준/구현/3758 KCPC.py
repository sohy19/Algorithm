t = int(input())
for _ in range(t):
  n, k, t, m = map(int, input().split())  # 팀 개수: n, 문제 개수: k, 당신 팀 ID: t, 로그 엔트리 개수: m
  
  scores = {}   # [ 각 팀의 각 문제에 대한 점수, 각 팀의 제출 횟수, 각 팀의 마지막 제출 시간 ]
  for i in range(1, n+1):
    scores[i] = [0] * (k + 2)

  for time in range(m):
    i, j, s = map(int, input().split())  # 팀 ID: i, 문제 번호: j, 획득한 점수: s

    if scores[i][j-1] < s:
      scores[i][j-1] = s
    scores[i][-2] += 1
    scores[i][-1] = time
  
  sum_scores = sorted(scores, key = lambda x:(-sum(scores[x][:k]), scores[x][-2], scores[x][-1]))
  print(sum_scores.index(t) + 1)
