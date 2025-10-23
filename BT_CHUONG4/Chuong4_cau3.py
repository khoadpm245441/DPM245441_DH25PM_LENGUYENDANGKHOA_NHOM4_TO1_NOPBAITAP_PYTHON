# giải bài tập chuơng 4 câu 3
def BMI(height, weight ):
    return weight/(height**2)
def PhanLoai(bmi):
    if bmi<18.5:
        return "gầy"
    elif    bmi<=24.9:
        return "bình thường"
    elif bmi<=29.9:
        return "hơi béo"
    elif bmi<=34.9: 
        return "Béo Phì Cấp Độ 1" 
    elif bmi<=39.9: 
        return "Béo Phì Cấp Độ 2" 
    else: 
        return "Béo Phì Cấp độ 3" 
def nguycobenh(bmi):
    if bmi<18.5:
        return "thấp"
    elif bmi<=24.9:
          return "Trung Bình" 
    elif bmi<=29.9: 
        return "Cao" 
    elif bmi<=34.9: 
        return "Cao" 
    elif bmi<=39.9: 
        return "Rất cao" 
    else: 
        return "Nguy Hiểm" 
print("nhập vào chiều cao:")
height=float (input())
print("nhập vào cân nặng: ")
weight=float(input())
bmi=BMI(height,weight)
print("BMI của bạn=",bmi) 
print("Phân loại bạn=",PhanLoai(bmi)) 
print("Nguy cơ bệnh của Thím=",nguycobenh(bmi))
