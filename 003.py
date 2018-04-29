target = 600851475143
i = 1
while target != 1:
  i += 2
  while target % i == 0:
    target /= i
print(i)