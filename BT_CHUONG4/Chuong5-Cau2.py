# =====================
# Câu: Tối ưu chuỗi
# =====================

def toi_uu_chuoi(s):
    # Tách chuỗi thành danh sách các từ, tự động bỏ khoảng trắng dư
    tu = s.split()
    # Ghép lại bằng 1 khoảng trắng duy nhất
    return " ".join(tu)

# Vòng lặp để người dùng có thể nhập nhiều lần
while True:
    s = input("Nhập chuỗi cần tối ưu: ")
    s_toi_uu = toi_uu_chuoi(s)
    print(" Chuỗi sau khi tối ưu:", s_toi_uu)

    tiep = input("Bạn có muốn nhập chuỗi khác không? (c/k): ").lower()
    if tiep != 'c':
        print("Cảm ơn bạn đã sử dụng chương trình! ")
        break
