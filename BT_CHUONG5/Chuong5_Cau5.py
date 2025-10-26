# Câu 5: Xử lý chuỗi với các hàm cơ bản

# Nhập chuỗi
chuoi = input("Nhập vào một chuỗi: ")

# Khởi tạo các biến đếm
hoa = thuong = so = ky_tu_dac_biet = khoang_trang = nguyen_am = phu_am = 0

# Tập hợp nguyên âm (cả chữ hoa và thường)
nguyen_am_set = "aeiouAEIOU"

# Duyệt từng ký tự trong chuỗi
for c in chuoi:
    if c.isupper():
        hoa += 1
    elif c.islower():
        thuong += 1

    if c.isdigit():
        so += 1
    elif not c.isalnum() and c != ' ':
        ky_tu_dac_biet += 1
    elif c.isspace():
        khoang_trang += 1

    # Kiểm tra nguyên âm / phụ âm
    if c.isalpha():
        if c in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

# Xuất kết quả
print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ là chữ số:", so)
print("Số ký tự đặc biệt:", ky_tu_dac_biet)
print("Số ký tự khoảng trắng:", khoang_trang)
print("Số chữ là nguyên âm:", nguyen_am)
print("Số chữ là phụ âm:", phu_am)
