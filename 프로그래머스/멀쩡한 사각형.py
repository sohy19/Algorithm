def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def solution(w,h):
    value = gcd(w, h)
    answer = w * h - (w + h - value)
    return answer
