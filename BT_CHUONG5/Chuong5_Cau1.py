# =====================
# Câu: Kiểm tra chuỗi đối xứng
# =====================

while True:
    # Nhập chuỗi
    s = input("Nhập chuỗi cần kiểm tra: ")

    # Chuẩn hóa: bỏ khoảng trắng, đổi về chữ thường
    s_clean = s.replace(" ", "").lower()

    # Kiểm tra đối xứng (palindrome)
    if s_clean == s_clean[::-1]:
        print("✅ Chuỗi là chuỗi đối xứng!")
    else:
        print("❌ Chuỗi không đối xứng.")

    # Hỏi người dùng có muốn tiếp tục không
    tiep = input("Bạn có muốn kiểm tra chuỗi khác không? (c/k): ").lower()
    if tiep != 'c':
        print("Cảm ơn bạn đã sử dụng chương trình! ")
        break

