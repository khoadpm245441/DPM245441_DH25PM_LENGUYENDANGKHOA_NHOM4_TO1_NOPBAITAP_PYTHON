import os

# Hàm 1: Lấy ra tên file nhạc kèm phần mở rộng (.mp3, .wav, ...)
def LayTenFile(day_duong_dan):
    return os.path.basename(day_duong_dan)

# Hàm 2: Lấy ra tên bài hát (bỏ phần mở rộng)
def LayTenBaiHat(day_duong_dan):
    ten_file = os.path.basename(day_duong_dan)
    ten_bai, _ = os.path.splitext(ten_file)
    return ten_bai


# -----------------------------
# Chương trình chính
duong_dan = input("Nhập đường dẫn file nhạc: ")

print("Tên file nhạc:", LayTenFile(duong_dan))
print("Tên bài hát:", LayTenBaiHat(duong_dan))
