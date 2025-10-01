print("Chương trình tính S(x, n) = x + x^2/2! + x^3/3! + ... + x^n/n!")

# Nhập dữ liệu
x = int(input("Nhập x: "))
n = int(input("Nhập n: "))

# Biến lưu tổng
S = 0

# Tính tổng
for i in range(1, n+1):
    # Tử số = x^i
    tu = x ** i
    
    # Mẫu số = i!
    mau = 1
    for j in range(1, i+1):
        mau *= j
    
    # Cộng vào tổng
    S += tu / mau

# Xuất kết quả
print(f"S({x}, {n}) = {S}")
