def contains_vowels(password):   # 모음(a,e,i,o,u) 하나 포함
  vowels = ("a", "e", "i", "o", "u")
  for char in password:
    if char in vowels:
        return True
  return False

def three_word(password):   # 모음 혹은 자음 3개 연속 X
  vowels = 0
  consonants = 0
  
  for char in password:
    if char in ("a", "e", "i", "o", "u"):
      vowels += 1
      if vowels == 3:
        return False
      consonants = 0
    else:
      consonants += 1
      if consonants == 3:
        return False
      vowels = 0

  return True

def two_word(password):   # 같은 글자 두 번 연속 X (o, e 제외)
  for i in range(len(password)-1):
    if password[i] == password[i+1]:
      if password[i] == "e" or password[i] == "o":
        continue
      else:
        return False
      
  return True

while True:
  password = input()

  if password == "end":
    break

  if contains_vowels(password) and three_word(password) and two_word(password):
    print(f'<{password}> is acceptable.')
  else:
    print(f'<{password}> is not acceptable.')
