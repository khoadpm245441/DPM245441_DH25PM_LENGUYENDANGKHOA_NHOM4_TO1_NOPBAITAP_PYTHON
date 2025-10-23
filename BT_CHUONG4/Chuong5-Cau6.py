# =====================
# Câu 6: Trích lọc số âm trong chuỗi
# =====================

import re  # Thư viện hỗ trợ tìm mẫu trong chuỗi (regular expressions)

def NegativeNumberInStrings(s):
    # Tìm tất cả các số nguyên âm trong chuỗi
    # Mẫu: dấu '-' theo sau là ít nhất một chữ số
    so_am = re.findall(r'-\d+', s)

    # In kết quả
    if so_am:
        print("Các số nguyên âm trong chuỗi là:", ', '.join(so_am))
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

# --- Chương trình chính ---
chuoi = input("Nhập chuỗi cần trích lọc: ")
NegativeNumberInStrings(chuoi)
