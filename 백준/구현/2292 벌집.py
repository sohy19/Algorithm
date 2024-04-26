n = int(input())

count = 1   # 지나는 방 개수
end = 1   # 라인의 벌집 끝값

while n > end:
    end += count * 6
    count += 1

print(count)
