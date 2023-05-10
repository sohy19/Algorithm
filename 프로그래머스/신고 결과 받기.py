def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    user_idx = {}   # 유저 별 인덱스
    report_cnt = {}   # 각 유저 별 신고 당한 횟수
    report_user = {}   # 각 유저를 신고한 유저 리스트
    for i in range(len(id_list)):
        user_idx[id_list[i]] = i
        report_cnt[id_list[i]] = 0
        report_user[id_list[i]] = []
    for r in report:
        user, reported_user = r.split()
        if user not in report_user[reported_user]:
            report_cnt[reported_user] += 1
            report_user[reported_user].append(user)
    for key in report_cnt:
        if report_cnt[key] >= k:
            for user in report_user[key]:
                answer[user_idx[user]] += 1
    return answer
