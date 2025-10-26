n = int(input("Nhập số lượng phần tử của dãy: "))
lst = []

for i in range(n):
    while True:
        x = int(input(f"Nhập phần tử thứ {i + 1}: "))
        # Nếu là phần tử đầu tiên, chấp nhận luôn
        if i == 0 or x > lst[-1]:
            lst.append(x)
            break
        else:
            print("❌ Số vừa nhập không lớn hơn số trước đó! Vui lòng nhập lại.")

print("✅ Dãy số tăng dần đã nhập là:", lst)
