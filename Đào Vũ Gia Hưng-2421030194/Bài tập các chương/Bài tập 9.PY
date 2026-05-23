a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

tong = a + b + c
tong_str = str(tong)
dem = 0
i = 0
while i < len(tong_str):
    if int(tong_str[i]) % 2 == 0:
        dem += 1
    i += 1

print(f"Tong a+b+c: {tong}")
print(f"So chu so chan trong tong: {dem}")