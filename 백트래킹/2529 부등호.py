import sys
input = sys.stdin.readline

number = int(input())   # 부등호 개수
sign = list(input().split())
original_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
min_num = sys.maxsize
max_num = 0

def find_num(arr, nums, now):
    global min_num, max_num
    if now == number:
        for n in nums:
            if n not in arr:
                arr.append(n)
                if int(''.join(arr)) < int(min_num):
                    min_num = ''.join(arr)
                if int(''.join(arr)) > int(max_num):
                    max_num = ''.join(arr)
                arr.pop()
        return
    for i in range(len(nums)):
        if nums[i] not in arr:
            arr.append(nums[i])
            if sign[now] == "<":
                find_num(arr, original_nums[int(nums[i])+1:], now+1)
                arr.pop()
            else:
                find_num(arr, original_nums[:int(nums[i])], now+1)
                arr.pop()

find_num([], original_nums, 0)
print(max_num)
print(min_num)