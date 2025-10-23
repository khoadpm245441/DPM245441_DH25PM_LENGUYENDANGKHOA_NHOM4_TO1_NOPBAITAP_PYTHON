#giải bài tập chương 3 câu 7   

def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
def ngay_ke_tiep(ngay, thang, nam):
    ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if la_nam_nhuan(nam):
        ngay_trong_thang[1] = 29  

    ngay += 1

    if ngay > ngay_trong_thang[thang - 1]:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
            nam += 1

    return ngay, thang, nam
def main():
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    ngay_tiep, thang_tiep, nam_tiep = ngay_ke_tiep(ngay, thang, nam)
    print(f"Ngày kế tiếp là: {ngay_tiep}/{thang_tiep}/{nam_tiep}")
if __name__ == "__main__":
    main()
