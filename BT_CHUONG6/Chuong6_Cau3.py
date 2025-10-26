import random

# ================================
# Câu 3: Xử lý List Đa Chiều
# ================================

# Nhập kích thước ma trận
m = int(input("Nhập số dòng (m): "))
n = int(input("Nhập số cột (n): "))

# 1. Khởi tạo ma trận MxN phần tử ngẫu nhiên
matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]

print("\nMa trận ngẫu nhiên:")
for row in matrix:
    print(row)

# 2. Xuất dòng bất kỳ nhập từ bàn phím
dong = int(input("\nNhập số dòng cần xuất (0 → {}): ".format(m-1)))
if 0 <= dong < m:
    print("Dòng", dong, "là:", matrix[dong])
else:
    print("❌ Dòng không hợp lệ!")

# 3. Xuất cột bất kỳ nhập từ bàn phím
cot = int(input("\nNhập số cột cần xuất (0 → {}): ".format(n-1)))
if 0 <= cot < n:
    cot_gia_tri = [matrix[i][cot] for i in range(m)]
    print("Cột", cot, "là:", cot_gia_tri)
else:
    print("❌ Cột không hợp lệ!")

# 4. Xuất số MAX trong ma trận
max_value = max(max(row) for row in matrix)
print("\n✅ Số lớn nhất (MAX) trong ma trận là:", max_value)
