# giải bài tập chuong 3 câu 19

import math

def S(x, n):
    s = 0
    for k in range(n+1):
        s += (x**(2*k+1)) / math.factorial(2*k+1)
    return s

# Nhập từ bàn phím
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

print("Giá trị S(x, n) =", S(x, n))