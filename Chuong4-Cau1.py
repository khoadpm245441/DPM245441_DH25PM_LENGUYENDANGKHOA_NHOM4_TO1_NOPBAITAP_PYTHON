from math import sqrt

def dien_tich_tam_giac(a, b, c):
    # Kiểm tra điều kiện hợp lệ của tam giác
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return None
    
    # Tính chu vi và nửa chu vi
    cv = a + b + c
    p = cv / 2

    # Công thức Heron
    dt = sqrt(p * (p - a) * (p - b) * (p - c))
    return dt

# --- Chương trình chính ---
print("Chương trình tính diện tích Tam Giác")
a = float(input("Nhập cạnh a > 0: "))
b = float(input("Nhập cạnh b > 0: "))
c = float(input("Nhập cạnh c > 0: "))

dt = dien_tich_tam_giac(a, b, c)

if dt is None:
    print("Tam giác không hợp lệ!")
else:
    print(f"Diện tích tam giác là: {dt:.2f}")
