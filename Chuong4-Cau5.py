# Hàm đệ qui trả về số Fibonacci tại vị trí N
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# Hàm đệ qui (hoặc kết hợp vòng lặp) trả về dãy Fibonacci từ 1 -> N
def fib_list(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        ds = fib_list(n - 1)  # lấy danh sách tới n-1
        ds.append(fib(n))     # thêm số thứ n
        return ds

# --- Chương trình chính ---
N = int(input("Nhập N: "))

print(f"Số Fibonacci tại vị trí {N} là: {fib(N)}")
print(f"Dãy Fibonacci từ 1 đến {N} là: {fib_list(N)}")
