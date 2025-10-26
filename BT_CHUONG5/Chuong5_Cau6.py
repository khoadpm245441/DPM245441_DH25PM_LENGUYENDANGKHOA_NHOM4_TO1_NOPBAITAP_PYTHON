import re

def NegativeNumberInStrings(s):
    # Tìm tất cả các số nguyên âm trong chuỗi
    # Mẫu regex: dấu '-' đi kèm với 1 hoặc nhiều chữ số, 
    # nhưng phải đảm bảo không có thêm dấu '-' liền trước (để tránh '--')
    negative_numbers = re.findall(r'(?<!-)-\d+', s)

    # Chuyển thành số nguyên
    negative_numbers = [int(num) for num in negative_numbers]

    # In kết quả
    if negative_numbers:
        print("Các số nguyên âm trong chuỗi là:", *negative_numbers)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

# -----------------------------
# Chương trình chính
chuoi = input("Nhập chuỗi: ")
NegativeNumberInStrings(chuoi)
