def is_beautiful():
    for i in range(n):
        if i == 0:
            now_num = ans[i]
            cnt = 1
        elif now_num == ans[i]:
            cnt += 1
        else:
            if cnt % now_num == 0:
                cnt = 1
                now_num = ans[i]
                continue
            else:
                return False
    if cnt % now_num == 0:
        return True

def choose_num(now):
    global cnt
    if now == n+1:
        if is_beautiful():
            cnt += 1
        return
    for i in range(1, 5):
        ans.append(i)
        choose_num(now+1)
        ans.pop()


n = int(input())
ans = []
cnt = 0
choose_num(1)
print(cnt)
