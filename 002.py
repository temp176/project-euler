i = 2
f = 0
pre = [1,2]
total = 2
while f < 4000001:
    f = pre[0] + pre[1]
    pre[0] = pre[1]
    pre[1] = f
    if f % 2 == 0 :
        total += f
print(total)