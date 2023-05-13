while True:
  triangle = sorted(list(map(int, input().split())))
  if triangle[0] == triangle[1] == triangle[2] == 0:
     break
  if triangle[0] + triangle[1] <= triangle[2]:   # 두 변의 길이가 가장 긴 변의 길이보다 길지 않은 경우  
    print('Invalid')
  elif triangle[0] == triangle[1] == triangle[2]:   # 세 변의 길이가 모두 같은 경우
    print('Equilateral')
  elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[2] == triangle[0]:   # 두 변의 길이만 같은 경우
    print('Isosceles')
  else:   # 세 변의 길이가 모두 다른 경우
    print('Scalene')
