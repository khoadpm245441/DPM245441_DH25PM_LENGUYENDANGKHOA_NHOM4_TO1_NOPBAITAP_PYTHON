# Câu 6: Minh họa ý nghĩa các toán tử trong Python

# Toán tử / : Chia lấy kết quả thực (float)
print("7 / 2 =", 7 / 2)     # 3.5

# Toán tử // : Chia lấy phần nguyên (floor division)
print("7 // 2 =", 7 // 2)   # 3

# Toán tử % : Chia lấy dư
print("7 % 2 =", 7 % 2)     # 1

# Toán tử ** : Lũy thừa
print("2 ** 3 =", 2 ** 3)   # 8

# Toán tử and : Cả hai điều kiện đúng thì True
print("True and False =", True and False)  # False
print("5 > 2 and 7 > 3 =", 5 > 2 and 7 > 3)  # True

# Toán tử or : Một trong hai điều kiện đúng thì True
print("True or False =", True or False)    # True
print("5 > 10 or 7 > 3 =", 5 > 10 or 7 > 3)  # True

# Toán tử is : Kiểm tra 2 biến có cùng trỏ đến một đối tượng trong bộ nhớ không
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a == b:", a == b)   # True (giá trị bằng nhau)
print("a is b:", a is b)   # False (khác đối tượng trong bộ nhớ)
print("a is c:", a is c)   # True (cùng một đối tượng)
