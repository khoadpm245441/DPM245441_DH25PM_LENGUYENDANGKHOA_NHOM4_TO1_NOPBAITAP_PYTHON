#Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím.
#Nhập một chuỗi
name = input("Nhập tên của bạn: ")
print("Xin chào", name)

#Nhập một số nguyên (int)
age = int(input("Nhập tuổi: "))
print("Tuổi của bạn là:", age)

#Nhập một số thực (float)
score = float(input("Nhập điểm trung bình: "))
print("Điểm của bạn:", score)

#Nhập nhiều giá trị trên một dòng (dùng split())
a, b = map(int, input("Nhập hai số cách nhau bởi dấu cách: ").split())
print("Tổng =", a + b)

#Nhập danh sách các số
numbers = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
print("Danh sách:", numbers)