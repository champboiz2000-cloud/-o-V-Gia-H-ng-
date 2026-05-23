s = "2 4 6 7 9"

b = s.split(" ")

for i in range(0, len(b)):
    b[i] = int(b[i])

print(b)