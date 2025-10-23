# =====================
# Câu 11
# =====================

def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s


def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s


def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s


# Trường hợp 1
def case1():
    print("Trường hợp 1:")
    global val
    val = 5
    print(sum1(5))  # 5
    print(sum2())   # 5
    print(sum3())   # 0


# Trường hợp 2
def case2():
    print("\nTrường hợp 2:")
    global val
    val = 5
    print(sum1(5))  # 5
    print(sum3())
