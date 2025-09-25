#Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.


#Lỗi cú pháp (Syntax Error)
#Xảy ra khi vi phạm quy tắc ngôn ngữ Python (thiếu dấu :, sai thụt lề, thiếu ngoặc...).

#Lỗi logic (Logic Error)
#Chương trình chạy được nhưng kết quả sai do sai ý tưởng hoặc công thức.

#Lỗi khi chạy (Runtime Error / Exception)
#Xảy ra trong quá trình thực thi, ví dụ chia cho 0, truy cập mảng ngoài phạm vi...


#Cách bắt lỗi trong Python
#Python cung cấp cấu trúc try...except để xử lý lỗi:
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    result = a / b
    print("Kết quả =", result)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ!")
except Exception as e:
    print("Lỗi khác:", e)
finally:
    print("Chương trình kết thúc.")