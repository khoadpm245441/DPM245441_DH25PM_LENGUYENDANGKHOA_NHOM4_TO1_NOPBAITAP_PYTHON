print("Chương trình xác định quý của tháng")

# Nhập tháng
thang = int(input("Nhập tháng (1-12): "))

# Kiểm tra quý
if 1 <= thang <= 3:
    print("Tháng", thang, "thuộc Quý 1")
elif 4 <= thang <= 6:
    print("Tháng", thang, "thuộc Quý 2")
elif 7 <= thang <= 9:
    print("Tháng", thang, "thuộc Quý 3")
elif 10 <= thang <= 12:
    print("Tháng", thang, "thuộc Quý 4")
else:
    print("Tháng không hợp lệ!")
