print("Chương trình tìm ngày kế tiếp")

# Hàm kiểm tra năm nhuận
def nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

# Hàm tìm số ngày trong tháng
def so_ngay_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if nam_nhuan(nam) else 28
    else:
        return 0  # tháng không hợp lệ

# Nhập dữ liệu
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tính ngày kế tiếp
ngay_max = so_ngay_thang(thang, nam)

if ngay < 1 or thang < 1 or thang > 12 or ngay > ngay_max:
    print("Ngày tháng năm không hợp lệ!")
else:
    ngay += 1
    if ngay > ngay_max:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
            nam += 1

    print("Ngày kế tiếp là:", ngay, "/", thang, "/", nam)
