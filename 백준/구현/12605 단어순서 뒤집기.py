n = int(input())
words = [list(input().split()) for _ in range(n)]

for i in range(n):
  print(f"Case #{i+1}: ", end="")
  for j in range(len(words[i])-1, -1, -1):
      print(words[i][j], end=" ")
  print()
