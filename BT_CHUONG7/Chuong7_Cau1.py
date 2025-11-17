import os

# --- 1. Các hàm xử lý file ---

def LuuFile(path, data):
    """Ghi dữ liệu sản phẩm (dưới dạng chuỗi) vào file."""
    # Mở file ở chế độ 'a' (append - ghi nối vào cuối)
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n") # Xuống dòng sau mỗi bản ghi
    file.close()

def DocFile(path):
    """Đọc dữ liệu từ file, phân tích cú pháp và trả về list sản phẩm."""
    arrProduct = []
    try:
        file = open(path, 'r', encoding='utf-8')
    except FileNotFoundError:
        return []

    for line in file:
        data = line.strip()
        if data:
            arr = data.split(';')
            
            # Kiểm tra và chuyển đổi giá tiền (chỉ số 2) sang float
            if len(arr) == 3:
                try:
                    arr[2] = float(arr[2])
                    arrProduct.append(arr)
                except ValueError:
                    continue

    file.close()
    return arrProduct

# --- 2. Các hàm chức năng chính ---

def XuatSanPham(dssp):
    """Xuất danh sách sản phẩm ra màn hình (Chức năng a)."""
    if not dssp:
        print("Danh sách sản phẩm trống.")
        return
        
    print("\n" + "=" * 40)
    print(f"| {'Mã SP':<8} | {'Tên Sản Phẩm':<20} | {'Giá (VNĐ)':<8} |")
    print("=" * 40)
    for row in dssp:
        # In các cột: Mã, Tên, Giá. Dùng định dạng float với 2 chữ số thập phân cho giá
        print(f"| {row[0]:<8} | {row[1]:<20} | {row[2]:<8.2f} |")
    print("=" * 40)


def SortSp(dssp):
    """Sắp xếp danh sách sản phẩm theo đơn giá giảm dần (Chức năng b)."""
    n = len(dssp)
    # Thuật toán Sắp xếp nổi bọt (Bubble Sort)
    for i in range(n):
        for j in range(i + 1, n): 
            # So sánh giá (chỉ số 2). Nếu dssp[i] < dssp[j] thì đổi chỗ để được giảm dần
            if dssp[i][2] < dssp[j][2]:
                # Đổi chỗ dssp[i] và dssp[j]
                dssp[i], dssp[j] = dssp[j], dssp[i]
    return dssp

# --- 3. Logic chính của chương trình (main) ---
FILE_PATH = "database.txt"

def main():
    print("<<< CHƯƠNG TRÌNH QUẢN LÝ SẢN PHẨM >>>")

    # --- NHẬP VÀ LƯU SẢN PHẨM ---
    print("\n--- 1. NHẬP THÔNG TIN SẢN PHẨM ---")
    
    masp = input("Nhập mã SP (Chuỗi): ")
    tensp = input("Nhập tên SP (Chuỗi): ")
    
    while True:
        try:
            dongia = float(input("Nhập giá (Số): "))
            break
        except ValueError:
            print("Lỗi: Đơn giá phải là một giá trị số.")

    # Tạo chuỗi dữ liệu
    line = masp + ";" + tensp + ";" + str(dongia)
    LuuFile(FILE_PATH, line)
    print(f"\n✅ Đã lưu sản phẩm '{tensp}' vào file '{FILE_PATH}' thành công.")
    
    print("-" * 40)

    # --- ĐỌC, XUẤT VÀ SẮP XẾP SẢN PHẨM ---
    
    dssp = DocFile(FILE_PATH)
    
    # a) Xuất danh sách sản phẩm
    print("\n--- 2. DANH SÁCH SẢN PHẨM TỪ FILE (TRƯỚC KHI SẮP XẾP) ---")
    XuatSanPham(dssp)

    # b) Sắp xếp và Xuất danh sách giảm dần
    if dssp:
        dssp_sorted = SortSp(dssp) 
        print("\n--- 3. DANH SÁCH SẢN PHẨM SAU KHI SẮP XẾP GIÁ GIẢM DẦN ---")
        XuatSanPham(dssp_sorted)
    else:
        print("Không có sản phẩm nào để sắp xếp.")

if __name__ == "__main__":
    main()