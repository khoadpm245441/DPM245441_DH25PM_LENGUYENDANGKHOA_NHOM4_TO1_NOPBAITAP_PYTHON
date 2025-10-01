print("Chương trình kiểm tra năm nhuận")

# Nhập năm từ bàn phím
year = int(input("Mời bạn nhập vào 1 năm: "))

# Điều kiện năm nhuận
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Năm", year, "là năm nhuận")
else:
    print("Năm", year, "không phải là năm nhuận")
