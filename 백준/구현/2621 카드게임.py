card = []
for i in range(5):
    card.append(input().split())   # 이중 리스트로 [색, 숫자] 저장
card.sort(key=lambda x:x[1])   # 숫자 기준으로 정렬

score = 0   # 점수
while True:
    # 첫 번째 조건
    if (card[0][0] == card[1][0] and card[1][0] == card[2][0] and card[2][0] == card[3][0] and card[3][0] == card[4][0]) and (int(card[0][1]) + 1 == int(card[1][1]) and int(card[0][1]) + 2 == int(card[2][1]) and int(card[0][1]) + 3 == int(card[3][1]) and int(card[0][1]) + 4 == int(card[4][1])) :
        score = int(card[4][1]) + 900
        break
    # 두 번째 조건
    elif (card[0][1] == card[1][1] and card[1][1] == card[2][1] and card[2][1] == card[3][1]) or (card[1][1] == card[2][1] and card[2][1] == card[3][1] and card[3][1] == card[4][1]):
        score = int(card[2][1]) + 800
        break
    # 세 번째 조건
    elif card[0][1] == card[1][1] and card[2][1] == card[3][1] and card[3][1] == card[4][1]:
        score = int(card[2][1])*10 + int(card[0][1]) + 700
        break
    elif card[0][1] == card[1][1] and card[1][1] == card[2][1] and card[3][1] == card[4][1]:
        score = int(card[2][1])*10 + int(card[4][1]) + 700
        break
    # 네 번째 조건
    elif card[0][0] == card[1][0] and card[1][0] == card[2][0] and card[2][0] == card[3][0] and card[3][0] == card[4][0]:
        score = int(card[4][1]) + 600
        break
    # 다섯 번째 조건
    elif int(card[0][1]) + 1 == int(card[1][1]) and int(card[0][1]) + 2 == int(card[2][1]) and int(card[0][1]) + 3 == int(card[3][1]) and int(card[0][1]) + 4 == int(card[4][1]):
        score = int(card[4][1]) + 500
        break
    # 여섯 번째 조건
    elif (card[0][1] == card[1][1] and card[1][1] == card[2][1]) or (card[1][1] == card[2][1] and card[2][1] == card[3][1]) or (card[2][1] == card[3][1] and card[3][1] == card[4][1]):
        score = int(card[2][1]) + 400
        break
    # 일곱 번째 조건
    elif card[0][1] == card[1][1] and card[2][1] == card[3][1]:
        score = int(card[2][1])*10 + int(card[0][1]) + 300
        break
    elif card[1][1] == card[2][1] and card[3][1] == card[4][1]:
        score = int(card[3][1])*10 + int(card[1][1]) + 300
        break
    elif card[0][1] == card[1][1] and card[3][1] == card[4][1]:
        score = int(card[3][1])*10 + int(card[0][1]) + 300
        break
    # 여덟 번째 조건
    elif card[0][1] == card[1][1]:
        score = int(card[0][1]) + 200
        break
    elif card[1][1] == card[2][1]:
        score = int(card[1][1]) + 200
        break
    elif card[2][1] == card[3][1]:
        score = int(card[2][1]) + 200
        break
    elif card[3][1] == card[4][1]:
        score = int(card[3][1]) + 200
        break
    # 아홉 번째 조건
    else:
        score = int(card[4][1]) + 100
        break

print(score)