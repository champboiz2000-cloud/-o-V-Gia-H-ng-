# Câu 1
print("Câu 1")
n = int(input("Nhập n: "))
day = []
for i in range(n):
    x = float(input(f"Nhập x{i+1}: "))
    day.append(x)

tong = 0
dem = 0
for x in day:
    if x > 0 and x < 1000:
        tong += x
        dem += 1

if dem > 0:
    print("Trung bình cộng:", tong / dem)
else:
    print("Không có phần tử nào thỏa điều kiện")

# Câu 2
print("Câu 2")
n = input("Nhập số nguyên dương n: ")

tong = 0
for chu_so in n:
    tong += int(chu_so)

if tong % 3 == 0:
    print("Tổng các chữ số chia hết cho 3")
else:
    print("Tổng các chữ số không chia hết cho 3")

# Câu 3
print("Câu 3")
n = input("Nhập số nguyên dương n: ")

tich = 1
for chu_so in n:
    tich *= int(chu_so)

if tich % 2 == 0 and tich > 20:
    print("Tích là số chẵn và lớn hơn 20")
else:
    print("Tích không thỏa điều kiện")

# Câu 4
print("Câu 4")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

tong = a + b
lon_nhat = 0
for chu_so in str(tong):
    if int(chu_so) > lon_nhat:
        lon_nhat = int(chu_so)

print("Tổng:", tong)
print("Chữ số lớn nhất trong tổng:", lon_nhat)

# Câu 5
print("Câu 5")
m = int(input("Nhập m: "))
n = input("Nhập n: ")

tong = 0
for chu_so in n:
    tong += int(chu_so)

if m % tong == 0:
    print(f"{m} chia hết cho tổng các chữ số của n ({tong})")
else:
    print(f"{m} không chia hết cho tổng các chữ số của n ({tong})")