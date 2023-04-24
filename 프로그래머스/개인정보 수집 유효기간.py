# 일자 넘었는지 확인
def overDate(year, mon, day, today):
    tYear, tMon, tDay = map(int, today.split("."))
    if year < tYear:
        return True
    elif year > tYear:
        return False
    elif mon < tMon:
        return True
    elif mon > tMon:
        return False
    elif day < tDay:
        return True
    elif day > tDay:
        return False
    else:
        return False

def solution(today, terms, privacies):
    answer = []
    
    # 약관 유효기간 딕셔너리 형태로 변경
    termsDit = {}
    for t in terms:
        type, mon = t.split()
        termsDit[type] = int(mon)
    
    # 파기해야 할 개인정보
    for i in range(len(privacies)):
        date, type = privacies[i].split()
        year, mon, day = map(int, date.split("."))
        # 유효기간
        mon += termsDit[type]   
        if mon > 12:   # 유효기간 더했을 때 12월을 넘어가는 경우
            if mon % 12 == 0:
                year += (mon // 12 - 1)
                mon = 12
            else:
              year += (mon // 12)
              mon -= (12 * (mon // 12))
        day -= 1
        if day == 0:   # 일자 하루 뺐을 때 0일일 경우
            mon -= 1
            day = 28
            if mon == 0:
                year -= 1
                mon = 12
        if overDate(year, mon, day, today):
            answer.append(i+1)
    return answer
