#giải bài tập chương 4 câu 7
import math

xa = float(input("Nhập vào xA: "))
ya = float(input("Nhập vào yA: "))
xb = float(input("Nhập vào xB: "))
yb = float(input("Nhập vào yB: "))

dab = math.sqrt((xb - xa)**2 + (yb - ya)**2)

print(f"Khoảng cách giữa A và B là: {dab:.2f}")
