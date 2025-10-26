def ToiUuDanhTu(chuoi):
    # Bước 1: Xóa khoảng trắng dư thừa ở đầu, cuối và giữa
    chuoi = chuoi.strip()                   # Xóa khoảng trắng đầu và cuối
    tu = chuoi.split()                      # Tách các từ (tự động bỏ khoảng trắng dư)
    
    # Bước 2: Viết hoa chữ cái đầu, còn lại viết thường
    tu = [word.capitalize() for word in tu]
    
    # Bước 3: Nối lại thành chuỗi hoàn chỉnh
    ket_qua = " ".join(tu)
    return ket_qua


# -----------------------------
# Chương trình chính
chuoi = input("Nhập chuỗi danh từ: ")
print("Chuỗi sau khi tối ưu:", ToiUuDanhTu(chuoi))
