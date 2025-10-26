import random

n = int(input("Nhập số lượng phần tử N: "))
lst = random.sample(range(1, 100), n)  # Lấy N số ngẫu nhiên KHÔNG trùng nhau trong khoảng 1–99

print("Danh sách ngẫu nhiên không trùng nhau là:", lst)
