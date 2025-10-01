print("Chương trình đọc số có tối đa 2 chữ số")

# Nhập số n
n = int(input("Nhập số n (0-99): "))

# Tạo danh sách chữ số
chu_so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

# Xử lý đọc số
if n < 0 or n > 99:
    print("Chỉ được nhập số từ 0 đến 99!")
elif n < 10:
    # Số có 1 chữ số
    if n == 0:
        print("Không")
    else:
        print(chu_so[n].capitalize())
else:
    chuc = n // 10
    donvi = n % 10

    # Đọc phần chục
    if chuc == 1:
        doc = "Mười"
    else:
        doc = chu_so[chuc].capitalize() + " mươi"

    # Đọc phần đơn vị
    if donvi == 0:
        pass  # không đọc gì
    elif donvi == 1:
        doc += " mốt" if chuc > 1 else " một"
    elif donvi == 5:
        doc += " lăm"
    else:
        doc += " " + chu_so[donvi]

    print(doc)
