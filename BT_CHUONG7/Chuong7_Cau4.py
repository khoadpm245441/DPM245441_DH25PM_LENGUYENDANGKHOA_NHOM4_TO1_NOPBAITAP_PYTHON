import json

# Chuỗi JSON đầu vào (Lưu ý: Chuỗi của bạn có vẻ bị sai định dạng JSON ở phần đầu và cuối: 
# {'..."} thay vì chỉ {"..."}. Tôi sẽ sửa lại chuỗi JSON hợp lệ.)

# Chuỗi JSON hợp lệ
json_string = '{"ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'

# 1. Chuyển đổi JSON String thành Python Object (Dictionary)
python_object = json.loads(json_string)

# 2. Xuất kết quả
print(f"Chuỗi JSON ban đầu: {json_string}")
print("-" * 40)
print(f"Đối tượng Python (type: {type(python_object)}):")
print(python_object)

# 3. Truy cập dữ liệu trong đối tượng Python
print(f"Giá trị 'ten': {python_object['ten']}")