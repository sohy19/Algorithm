a, b = input().split()

if int(''.join(reversed(a))) < int(''.join(reversed(b))):
  print(''.join(reversed(b)))
else:
  print(''.join(reversed(a)))
