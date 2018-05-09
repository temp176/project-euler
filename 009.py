CF = True
for m in range(1000):
    for n in range(1000):
        a = (m ** 2) - (n ** 2)
        b = 2 * m * n
        c = (m ** 2) + (n ** 2)
        if a < 0 or b < 0 or c < 0:
            break
        if a + b + c == 1000:
            print('(',a,b,c,')')
            print(a * b * c)
            CF = False
            break
    if CF == False:
        break
print('終了')
