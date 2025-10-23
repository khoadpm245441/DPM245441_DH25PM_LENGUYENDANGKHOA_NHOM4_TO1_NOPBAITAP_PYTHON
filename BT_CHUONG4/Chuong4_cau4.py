#giải bài tập chuơng 4 câu 4
def ROI(dt,cp):
    return (dt-cp)/cp
def GoiYDauTu(ROI):
    if roi>=0.75:
        return "Mua"
    else:
        return "Khong mua"

print("Chương trình tính ROI") 
dt=int(input("Nhập Doanh Thu:")) 
cp=int(input("Nhập chi phí:")) 
roi=ROI(dt,cp) 
print("Tỉ Lệ ROI=",roi) 
print("==>",GoiYDauTu(roi))
