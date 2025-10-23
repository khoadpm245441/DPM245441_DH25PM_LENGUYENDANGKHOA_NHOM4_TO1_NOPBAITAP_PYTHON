# trả lời câu hỏi số 1 chương 3

print("Chương trình kiểm tra năm nhuận")
year = int(input("Mời bạn nhập vào một năm: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Năm", year, "là năm nhuận")
else:
    print("Năm", year, "không nhuận")
