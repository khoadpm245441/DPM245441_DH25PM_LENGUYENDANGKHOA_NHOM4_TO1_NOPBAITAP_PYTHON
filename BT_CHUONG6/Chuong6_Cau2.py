
import random

# ================================
# Câu 2: Xử lý List nhập ngẫu nhiên
# ================================

# Hàm kiểm tra list có đối xứng không
def la_doi_xung(lst):
    return lst == lst[::-1]

# 1. Khởi tạo list ngẫu nhiên n phần tử
n = int(input("Nhập số phần tử cần tạo ngẫu nhiên: "))
lst = [random.randint(-10, 10) for _ in range(n)]
print("List ngẫu nhiên:", lst)

# 2. Nhập số k và xóa tất cả phần tử có giá trị k trong list
k = int(input("Nhập giá trị k cần xóa: "))
lst = [x for x in lst if x != k]
print("List sau khi xóa tất cả phần tử có giá trị", k, "là:", lst)

# 3. Kiểm tra list có đối xứng hay không
if la_doi_xung(lst):
    print("✅ List đối xứng!")
else:
    print("❌ List không đối xứng.")
