import os

def lay_ten_file_du_day(duong_dan):
    """Hàm lấy tên file bao gồm phần mở rộng (ví dụ: muabui.mp3)"""
    return os.path.basename(duong_dan)

def lay_ten_file_khong_duoi(duong_dan):
    """Hàm lấy tên file không bao gồm phần mở rộng (ví dụ: muabui)"""
    return os.path.splitext(os.path.basename(duong_dan))[0]

# Ví dụ sử dụng
duong_dan = r"d:\music\muabui.mp3"

print(lay_ten_file_du_day(duong_dan))      # 👉 Kết quả: muabui.mp3
print(lay_ten_file_khong_duoi(duong_dan))  # 👉 Kết quả: muabui

