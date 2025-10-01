#Câu 19: Tính giá trị biểu thức S
# tính S(x,n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!
def S(x, n):
    term = x        # term_k khi k=0: x^(2*0+1)/(2*0+1)! = x/1 = x
    total = term
    for k in range(0, n):   # sẽ tính thêm term_{k+1} từ term_k
        # chuyển sang term_{k+1}:
        term = term * x * x / ((2*k+2) * (2*k+3))
        total += term
    return total

# Ví dụ sử dụng
if __name__ == "__main__":
    x = float(input("Nhập x: "))
    n = int(input("Nhập n (số bậc, >=0): "))
    print("S(x,n) = {:.12f}".format(S(x, n)))

    # kiểm tra với hàm sinh (nhiều ngôn ngữ có math.sinh)
    import math
    print("sinh(x) (tham khảo) = {:.12f}".format(math.sinh(x)))

