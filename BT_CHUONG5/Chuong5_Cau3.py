def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Nhập chuỗi ---
s = input("Nhập chuỗi số (cách nhau bởi dấu ;): ")

# --- Tách chuỗi thành danh sách ---
arr = s.split(';')

# --- Chuyển thành danh sách số nguyên ---
numbers = []
for x in arr:
    try:
        numbers.append(int(x))
    except:
        pass  # bỏ qua nếu có ký tự không hợp lệ

# --- Xuất các số ---
print("\nCác số trong chuỗi:")
for n in numbers:
    print(n)

# --- Đếm số chẵn ---
so_chan = sum(1 for n in numbers if n % 2 == 0)

# --- Đếm số âm ---
so_am = sum(1 for n in numbers if n < 0)

# --- Đếm số nguyên tố ---
so_nguyen_to = sum(1 for n in numbers if la_so_nguyen_to(n))

# --- Tính giá trị trung bình ---
if len(numbers) > 0:
    trung_binh = sum(numbers) / len(numbers)
else:
    trung_binh = 0

# --- Xuất kết quả ---
print("\n📊 Kết quả thống kê:")
print("Số lượng chữ số chẵn:", so_chan)
print("Số lượng số âm:", so_am)
print("Số lượng số nguyên tố:", so_nguyen_to)
print("Giá trị trung bình:", round(trung_binh, 2))
