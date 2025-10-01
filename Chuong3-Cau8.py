print("Chương trình tính toán đơn giản")

# Nhập dữ liệu
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
pt = input("Nhập phép toán (+, -, *, /): ")

# Xử lý phép toán
if pt == "+":
    kq = a + b
elif pt == "-":
    kq = a - b
elif pt == "*":
    kq = a * b
elif pt == "/":
    if b != 0:
        kq = a / b
    else:
        kq = "Lỗi! Không thể chia cho 0."
else:
    kq = "Phép toán không hợp lệ!"

# Xuất kết quả
print("Kết quả:", kq)
