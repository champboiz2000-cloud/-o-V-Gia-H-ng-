a = [-20, -5, -100, 7, -50]

tong = 0
sl = 0

for x in a:
    if x < -10 and x > -1000:
        tong = tong + x
        sl = sl + 1

print(tong / sl)