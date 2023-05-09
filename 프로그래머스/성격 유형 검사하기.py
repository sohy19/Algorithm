def solution(survey, choices):
    personality = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0 }
    answer = ''
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] > 4:
            personality[survey[i][1]] += (choices[i] - 4)
        else:
            personality[survey[i][0]] += (4 - choices[i])
    idx = 1
    for key in personality.keys():
        if idx % 2 == 0:
            if personality[key] > personality[before_key]:
                answer = answer + key
            else:
                answer = answer + before_key
        else:
            before_key = key
        idx += 1
    return answer
