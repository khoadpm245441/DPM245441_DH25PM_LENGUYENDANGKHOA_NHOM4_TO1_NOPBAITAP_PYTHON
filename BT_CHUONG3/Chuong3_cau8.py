# giải bài tập chương 3 câu 8
def main():
    a= float(input("Nhập số a: "))
    b= float(input("Nhập số b: "))  
    pt = input("Nhập phép toán (+, -, *, /): ")

    if pt == '+':
        ketqua = a + b
    elif pt == '-':
        ketqua = a - b
    elif pt == '*':
        ketqua = a * b
    elif pt == '/':
        if b != 0:
            ketqua = a / b
        else:
            print("Lỗi: Không thể chia cho 0.")
            return
    else:
        print("Lỗi: Phép toán không hợp lệ.")
        return
    print(f"ketqua: {a} {pt} {b} = {ketqua}")

if __name__ == "__main__": 
    main()