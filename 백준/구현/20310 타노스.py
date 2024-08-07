nums = input()
zero = 0
one = 0

for i in range(len(nums)):
  if nums[i] == "0":
    zero += 1
  else:
    one += 1

output_zero = 0   
throw_one = 0

# 0은 반 넘기 전까지 먼저 출력
# 1은 반 먼저 버리고 나머지 반 출력
for i in range(len(nums)):
  if nums[i] == "0":
    if output_zero < zero // 2:
      print("0", end='')
      output_zero += 1
  else:
    if throw_one >= one // 2:
      print("1", end='')
    else:
      throw_one += 1
