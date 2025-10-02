def BMI(height, weight):
    return weight / (height ** 2)

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <= 24.9:
        return "Bình thường"
    elif bmi <= 29.9:
        return "Hơi Béo"
    elif bmi <= 34.9:
        return "Béo Phì Cấp Độ 1"
    elif bmi <= 39.9:
        return "Béo Phì Cấp Độ 2"
    else:
        return "Béo Phì Cấp Độ 3"

def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <= 24.9:
        return "Trung bình"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Nguy hiểm"

# --- Chương trình chính ---
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = BMI(height, weight)
print(f"\n📊 BMI = {bmi:.2f}")
print(f"➡️ Phân loại: {PhanLoai(bmi)}")
print(f"⚠️ Nguy cơ bệnh: {NguyCoBenh(bmi)}")
