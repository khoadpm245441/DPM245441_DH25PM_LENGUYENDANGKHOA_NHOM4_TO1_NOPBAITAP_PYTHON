# =====================
# Câu 5: Xử lý chuỗi với các hàm cơ bản
# =====================

# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi cần kiểm tra: ")

# Khởi tạo các biến đếm
hoa = thuong = so = kytu = khoang_trang = nguyen_am = phu_am = 0

# Tập hợp các nguyên âm
nguyen_am_set = "aeiouAEIOU"

# Duyệt từng ký tự trong chuỗi
for ch in s:
    if ch.isupper():             # Chữ in hoa
        hoa += 1
    elif ch.islower():           # Chữ in thường
        thuong += 1
    elif ch.isdigit():           # Chữ số
        so += 1
    elif ch.isspace():           # Khoảng trắng
        khoang_trang += 1
    else:                        # Ký tự đặc biệt
        kytu += 1

    # Kiểm tra nguyên âm / phụ âm (chỉ tính chữ cái)
    if ch.isalpha():
        if ch in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

# Xuất kết quả
print("\n Kết quả phân tích chuỗi:")
print(" Số chữ IN HOA:", hoa)
print(" Số chữ in thường:", thuong)
print(" Số ký tự là chữ số:", so)
print(" Số ký tự đặc biệt:", kytu)
print("␣ Số ký tự là khoảng trắng:", khoang_trang)
print("🅰 Số chữ là nguyên âm:", nguyen_am)
print("🅱 Số chữ là phụ âm:", phu_am)
