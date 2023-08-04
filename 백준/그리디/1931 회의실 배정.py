import sys
input = sys.stdin.readline

n = int(input())   # 회의 수
meetings = [tuple(map(int, input().split())) for _ in range(n)]   # (회의 시작 시간, 회의 끝 시간)

meetings.sort(key=lambda x: (x[1], x[0]))   # 회의 끝나는 시간 기준으로 오름차순 정렬
cnt = 1   # 첫 번째 회의 무조건 사용
end_time = meetings[0][1]
for i in range(1, n):
    if end_time <= meetings[i][0]:   # 이전 회의가 끝나는 시간 이후에 회의가 시작할 경우
        end_time = meetings[i][1]
        cnt += 1

print(cnt)
