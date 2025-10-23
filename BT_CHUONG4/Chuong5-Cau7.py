# =====================
# Câu 7: Tối ưu chuỗi danh từ
# =====================

def toi_uu_danh_tu(s):
    # B1: Xóa khoảng trắng dư thừa ở đầu và cuối
    s = s.strip()

    # B2: Tách chuỗi thành danh sách các từ (split() tự loại bỏ khoảng trắng dư)
    tu = s.split()

    # B3: Viết hoa ký tự đầu mỗi từ, phần còn lại viết thường
    tu_toi_uu = [word.capitalize() for word in tu]

    # B4: Ghép các từ lại thành chuỗi, mỗi từ cách nhau 1 khoảng trắng
    return " ".join(tu_toi_uu)


# --- Chương trình chính ---
chuoi = input("Nhập chuỗi danh từ cần tối ưu: ")
ket_qua = toi_uu_danh_tu(chuoi)
print(" Chuỗi sau khi tối ưu:", ket_qua)
