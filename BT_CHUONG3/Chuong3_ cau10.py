# giải bài tập chương 3 câu 10

from py_compile import main


x = int(input("Nhập x: "))
n= int(input("Nhập n: "))
s=0
for i in range(1,n+1):
    tu= x**i
    mau=1
    for j in range(1,i+1):
        mau *= j
    s += tu/mau
print("a({0},{1}) = {2}".format(x,n,s))
if __name__ == "__main__":
    main() 