x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
z = int(input("Nhap z: "))

tich = x * y * z
tich_str = str(tich)

# Dem so chu so
so_chu_so = 0
i = 0
while i < len(tich_str):
    so_chu_so += 1
    i += 1

# Tim chu so lon nhat
lon_nhat = 0
i = 0
while i < len(tich_str):
    chu_so = int(tich_str[i])
    if chu_so > lon_nhat:
        lon_nhat = chu_so
    i += 1

print(f"Tich x*y*z: {tich}")
print(f"So chu so: {so_chu_so}")
print(f"Chu so lon nhat: {lon_nhat}")