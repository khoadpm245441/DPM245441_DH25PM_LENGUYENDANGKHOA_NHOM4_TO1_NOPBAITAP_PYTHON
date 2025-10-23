# giải bài tập chương 3 câu 11

while True:
    n=int (input("nhap mot so nguyen duong: "))
    dem=0
    for i in range(1,n+1):
        if n % i==0:
            dem+=1
    if dem==2:
        print(n,"la so nguyen to")
    else:
        print(n,"khong phai la so nguyen to")
    hoi=input ("tiep tục??? (c/k): ")
    if hoi == "k":
        break
print("bye bye")