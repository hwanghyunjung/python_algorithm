T = [25, 5]
count = 0
while T[0] > 1 :
    if T[0] % T[1] == 0:
        T[0] /= T[1]
        count += 1
    else :
        T[0] -= 1
        count += 1
print(count)

