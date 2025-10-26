import math

# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Nhập mảng
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# 1. Các số lẻ
le = [x for x in M if x % 2 != 0]
# 2. Các số chẵn
chan = [x for x in M if x % 2 == 0]
# 3. Các số nguyên tố
nguyen_to = [x for x in M if la_so_nguyen_to(x)]
# 4. Các số không phải là số nguyên tố
khong_nguyen_to = [x for x in M if not la_so_nguyen_to(x)]

# Xuất kết quả
print("Dãy số ban đầu:", M)
print("-------------------------------------------------")
print("Dòng 1: Các số lẻ:", le, f"=> Có {len(le)} số lẻ")
print("Dòng 2: Các số chẵn:", chan, f"=> Có {len(chan)} số chẵn")
print("Dòng 3: Các số nguyên tố:", nguyen_to)
print("Dòng 4: Các số không phải là số nguyên tố:", khong_nguyen_to)
