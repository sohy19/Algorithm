code = input()
case = [0 for i in range(len(code))]

for i in range(len(code)):
    if i == 0:
        if code[i] != '0':
            case[i] = (1, 0)    # (문자 하나로 해석할 경우, 문자 두 개로 해석할 경우)
        else:
            case[len(code)-1] = (0, 0)  # 코드 맨 앞자리가 0인 경우는 잘못된 코드 (해석할 수 있는 방법이 없음)
            break
    else:
        c = code[i-1] + code[i]
        if code[i] == '0':
            if c != '10' and c != '20': # 코드 중간에 0이 있을 경우, 앞자리가 1이나 2여서 같이 해석하는 방법밖에 없다.
                case[len(code)-1] = (0, 0)
                break
            else:
                case[i] = (0, case[i-1][0])
        else:    
            #try:
                if int(c) < 27:
                    case[i] = (case[i-1][0] + case[i-1][1], case[i-1][0])
                else:
                    case[i] = (case[i-1][0] + case[i-1][1], 0)
            #except:
            #    case[len(code)-1] = (0, 0)
            #    break
result = case[len(code)-1][0] + case[len(code)-1][1]
print(result%1000000)
