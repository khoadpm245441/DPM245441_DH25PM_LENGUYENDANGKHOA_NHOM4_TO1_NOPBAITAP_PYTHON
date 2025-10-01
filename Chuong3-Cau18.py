n = int(input("Nhập n: "))

# Hình 1: Hình vuông rỗng
print("Hình 1:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 2: Tam giác vuông (góc dưới phải)
print("\nHình 2:")
for i in range(1, n+1):
    print("  " * (n-i) + "* " * i)

# Hình 3: Hình chữ Z
print("\nHình 3:")
for i in range(1, n):
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(2*n-1):
    print("*", end=" ")
print()


for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
