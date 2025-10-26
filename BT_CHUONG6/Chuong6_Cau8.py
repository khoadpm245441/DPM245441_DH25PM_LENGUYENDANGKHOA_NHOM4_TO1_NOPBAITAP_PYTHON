n = int(input("Nhập số phần tử của dãy: "))
M = []

for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

# Sắp xếp giảm dần
M.sort(reverse=True)

print("✅ Dãy sau khi sắp xếp giảm dần là:")
for i in range(n):
    print(f"M[{i}] = {M[i]}")
