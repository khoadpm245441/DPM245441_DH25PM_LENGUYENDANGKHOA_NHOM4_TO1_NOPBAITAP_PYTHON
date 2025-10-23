# =====================
# Câu 13
# =====================

def tong_uoc_so(n):
    """Trả về tổng các ước số của n (không kể chính n)"""
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


def la_so_hoan_thien(n):
    """Kiểm tra số hoàn thiện"""
    return tong_uoc_so(n) == n


def la_so_thinh_vuong(n):
    """Kiểm tra số thịnh vượng"""
    return tong_uoc_so(n) > n


# Kiểm thử
print("\nKết quả Câu 13:")
for num in [6, 12, 28, 15]:
    print(f"{num}: hoàn thiện = {la_so_hoan_thien(num)}, thịnh vượng = {la_so_thinh_vuong(num)}")
