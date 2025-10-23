#giải bài tập chuơng 4 câu 8

import math

a = float(input("Nhập vào a: "))
x = float(input("Nhập vào x: "))

if a > 0 and x >= 0:
    logax = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {logax:.4f}")
else:
    print("Giá trị của a phải lớn hơn 0 và x phải lớn hơn hoặc bằng 0.")
    