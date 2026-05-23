f = open("e:\\matran.txt", "r")
ma = [dong.split() for dong in f]
print(ma)

s = 0
for dong in ma:
    for gia_tri in dong:
        s += float(gia_tri)

print("Tổng ma trận là:", s)
f.close()