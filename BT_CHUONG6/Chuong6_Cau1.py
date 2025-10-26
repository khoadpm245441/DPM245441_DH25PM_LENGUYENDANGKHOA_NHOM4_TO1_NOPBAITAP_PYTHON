# ================================
# Câu 1: Xử lý List
# ================================

# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Khởi tạo list rỗng
ds = []

while True:
    print("\n--- MENU ---")
    print("1. Thêm phần tử vào list")
    print("2. Hiển thị list")
    print("3. Kiểm tra 1 số k xuất hiện bao nhiêu lần trong list")
    print("4. Tính tổng các số nguyên tố trong list")
    print("5. Sắp xếp list tăng dần")
    print("6. Xóa toàn bộ list")
    print("0. Thoát")

    chon = input("Nhập lựa chọn của bạn: ")

    if chon == "1":
        n = int(input("Nhập số cần thêm vào list: "))
        ds.append(n)
        print("=> Đã thêm", n)

    elif chon == "2":
        print("List hiện tại:", ds)

    elif chon == "3":
        k = int(input("Nhập số k cần kiểm tra: "))
        dem = ds.count(k)
        print(f"Số {k} xuất hiện {dem} lần trong list")

    elif chon == "4":
        tong_nt = sum(x for x in ds if la_so_nguyen_to(x))
        print("Tổng các số nguyên tố trong list là:", tong_nt)

    elif chon == "5":
        ds.sort()
        print("List sau khi sắp xếp tăng dần:", ds)

    elif chon == "6":
        ds.clear()
        print("=> Đã xóa toàn bộ list")

    elif chon == "0":
        print("Kết thúc chương trình.")
