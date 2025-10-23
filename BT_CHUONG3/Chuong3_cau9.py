# g giải bài tập chương 3 câu 9

def main():
    thang = int(input("Nhập tháng (1-12): "))   

    if 1<= thang <= 3:
        print(f"thang {thang} là Quý 1  ")
    elif 4 <= thang <= 6:
        print(f"thang {thang} là Quý 2  ")
    elif 7 <= thang <= 9:
        print(f"thang {thang} là Quý 3  ")
    elif 10 <= thang <= 12:
        print(f"thang {thang} là Quý 4  ")
    else:
        print("Lỗi: Tháng không hợp lệ. Vui lòng nhập số từ 1 đến 12.") 
if __name__ == "__main__":
    main()