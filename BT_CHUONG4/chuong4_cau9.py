#giải bài tập câu 9 chương 4

import math

n= int(input("nhập n: "))

s=0
for i in range(n): 
    s = math.sqrt(2+s)
print(f"s{n} = {s:.6f}")
