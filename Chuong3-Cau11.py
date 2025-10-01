print("Chương trình kiểm tra số nguyên tố")

def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # chỉ cần duyệt tới căn bậc 2 của n
        if n % i == 0:
            return False
    return True

while True:
    n = int(input("Nhập một số: "))

    if la_nguyen_to(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

    tiep_tuc = input("Bạn có muốn tiếp tục? (c/k): ")
    if tiep_tuc.lower() != "c":   # nếu không nhập 'c' thì thoát
        print("Thoát chương trình.")
        break
