2.5 
3.7
5.8
4.12
3.4
7.99
f = open("e:\\matran.txt", "r")
ma = []
ma = [dong.split() for dong in f]
print(ma)
s = 0
for subama in ma:
    for i in subama:
        s = s + float(i)
print("Tong cua ma tran la:", s)