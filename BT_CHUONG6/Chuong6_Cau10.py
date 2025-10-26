# Hàm nhập ma trận
def nhap_ma_tran(ten):
    dong = int(input(f"Nhập số dòng của ma trận {ten}: "))
    cot = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    matrix = []
    for i in range(dong):
        hang = []
        for j in range(cot):
            x = int(input(f"{ten}[{i}][{j}] = "))
            hang.append(x)
        matrix.append(hang)
    return matrix, dong, cot


# Hàm in ma trận
def in_ma_tran(matrix):
    for hang in matrix:
        print(" ".join(f"{x:4d}" for x in hang))
    print()


# Hàm cộng hai ma trận
def cong_ma_tran(A, B):
    dong = len(A)
    cot = len(A[0])
    C = []
    for i in range(dong):
        hang = []
        for j in range(cot):
            hang.append(A[i][j] + B[i][j])
        C.append(hang)
    return C


# Hàm tính ma trận chuyển vị
def chuyen_vi(A):
    dong = len(A)
    cot = len(A[0])
    T = []
    for j in range(cot):
        hang = []
        for i in range(dong):
            hang.append(A[i][j])
        T.append(hang)
    return T


# ======== CHƯƠNG TRÌNH CHÍNH ========

A, m, n = nhap_ma_tran("A")
B, m2, n2 = nhap_ma_tran("B")

if m != m2 or n != n2:
    print("Hai ma trận không cùng kích thước, không thể cộng được!")
else:
    print("\nMa trận A:")
    in_ma_tran(A)

    print("Ma trận B:")
    in_ma_tran(B)

    # Cộng 2 ma trận
    C = cong_ma_tran(A, B)
    print("Tổng hai ma trận A + B là:")
    in_ma_tran(C)

    # Chuyển vị
    AT = chuyen_vi(A)
    BT = chuyen_vi(B)

    print("Ma trận chuyển vị của A:")
    in_ma_tran(AT)

    print("Ma trận chuyển vị của B:")
    in_ma_tran(BT)
