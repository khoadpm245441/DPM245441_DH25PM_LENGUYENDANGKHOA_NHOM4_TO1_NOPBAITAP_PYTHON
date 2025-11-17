import json

# Đối tượng Python đầu vào (Dictionary)
pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}

# 1. Chuyển đổi Python Object (Dictionary) thành JSON String
# dumps (dump string)
json_string = json.dumps(pythonObject)

# 2. Xuất kết quả
print(f"Đối tượng Python ban đầu (type: {type(pythonObject)}):")
print(pythonObject)
print("-" * 40)
print(f"Chuỗi JSON sau khi chuyển đổi (type: {type(json_string)}):")
print(json_string)

# 3. Xuất kết quả với định dạng dễ đọc hơn (sử dụng indent)
print("\nChuỗi JSON với định dạng (indent=4):")
json_formatted = json.dumps(pythonObject, indent=4, ensure_ascii=False)
print(json_formatted)