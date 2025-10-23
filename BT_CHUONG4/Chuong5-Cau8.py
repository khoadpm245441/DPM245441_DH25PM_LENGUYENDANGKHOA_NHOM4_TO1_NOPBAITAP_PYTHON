# =====================
# Câu: Tách lấy tên bài hát
# =====================

import os  # Thư viện hỗ trợ xử lý đường dẫn file

def lay_ten_day_du(duong_dan):
    """Hàm lấy tên file nhạc có cả phần mở rộng (đuôi .mp3, .wav, ...)"""
    return os.path.basename(duong_dan)

def lay_ten_khong_duoi(duong_dan):
    """Hàm lấy tên file nhạc KHÔNG có phần mở rộng"""
    ten_day_du = os.path.basename(duong_dan)
    ten_khong_duoi, _ = os.path.splitext(ten_day_du)
    return ten_khong_duoi


# --- Chương trình chính ---
duong_dan = input("Nhập đường dẫn file nhạc: ")

print("🎵 Tên file đầy đủ:", lay_ten_day_du(duong_dan))
print("🎶 Tên bài hát:", lay_ten_khong_duoi(duong_dan))
