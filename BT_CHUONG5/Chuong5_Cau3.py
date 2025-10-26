# =====================
# Câu 3: Xử lý Tách chuỗi
# =====================

def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi số (cách nhau bằng dấu ';'): ")

# Tách chuỗi thành danh sách số nguyên
ds = [int(x) for x in s.split(';')]

# Xuất các số trên các dòng riêng biệt
print("\nCác số trong chuỗi:")
for x in ds:
    print(x)

# Đếm số chẵn
chan = sum(1 for x in ds if x % 2 == 0)

# Đếm số âm
am = sum(1 for x in ds if x < 0)

# Đếm số nguyên tố
nguyento = sum(1 for x in ds if la_nguyen_to(x))

# Tính giá trị trung bình
trung_binh = sum(ds) / len(ds)

# Xuất kết quả
print("\n Có", chan, "số chẵn")
print(" Có", am, "số âm")
print(" Có", nguyento, "số nguyên tố")
print(" Giá trị trung bình là:", round(trung_binh, 2))
