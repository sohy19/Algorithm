word = input()
dic = {}
max_num = 0
max_word = ""

for w in word:
    w = w.upper()
    if w in dic:
        dic[w] += 1
    else:
        dic[w] = 1
    if dic[w] > max_num:
        max_num = dic[w]
        max_word = w
    elif dic[w] == max_num:
        max_word = "?"

print(max_word)
