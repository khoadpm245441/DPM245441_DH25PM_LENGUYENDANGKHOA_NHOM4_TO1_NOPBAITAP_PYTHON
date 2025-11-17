import os

FILE_PATH = "product_management.txt"
# Cấu trúc dữ liệu trong bộ nhớ:
# {
#     'CAT': {'ma1': {'ten': 'Tên DM 1'}, ...},
#     'PROD': [{'ma': 'sp1', 'ten': 'Tên SP 1', 'gia': 1000.0, 'ma_dm': 'ma1'}, ...]
# }
DATA = {'CAT': {}, 'PROD': []}


# =================================================================
# I. CHỨC NĂNG XỬ LÝ FILE (ĐỌC & GHI)
# =================================================================

def DocFile():
    """Đọc dữ liệu từ file và tải vào biến DATA trong bộ nhớ."""
    global DATA
    DATA = {'CAT': {}, 'PROD': []}
    
    if not os.path.exists(FILE_PATH):
        return

    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(';')
                obj_type = parts[0]
                
                if obj_type == 'CAT' and len(parts) == 3:
                    ma, ten = parts[1], parts[2]
                    DATA['CAT'][ma] = {'ten': ten}
                
                elif obj_type == 'PROD' and len(parts) == 5:
                    try:
                        ma, ten, gia_str, ma_dm = parts[1], parts[2], parts[3], parts[4]
                        gia = float(gia_str)
                        DATA['PROD'].append({
                            'ma': ma, 
                            'ten': ten, 
                            'gia': gia, 
                            'ma_dm': ma_dm
                        })
                    except ValueError:
                        print(f"Cảnh báo: Dữ liệu giá không hợp lệ tại dòng: {line}")
                        
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

def LuuFile():
    """Lưu dữ liệu từ bộ nhớ (biến DATA) ra file."""
    lines = []
    
    # Lưu Danh mục
    for ma, cat in DATA['CAT'].items():
        lines.append(f"CAT;{ma};{cat['ten']}")
        
    # Lưu Sản phẩm
    for prod in DATA['PROD']:
        lines.append(f"PROD;{prod['ma']};{prod['ten']};{prod['gia']};{prod['ma_dm']}")
        
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            file.write('\n'.join(lines) + '\n')
        print(f"\n✅ Đã lưu dữ liệu thành công vào file '{FILE_PATH}'.")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

# =================================================================
# II. CHỨC NĂNG XỬ LÝ DỮ LIỆU (CRUD)
# =================================================================

def find_product_by_ma(ma_sp):
    """Tìm sản phẩm theo mã."""
    for prod in DATA['PROD']:
        if prod['ma'] == ma_sp:
            return prod
    return None

def find_cat_by_ma(ma_dm):
    """Tìm danh mục theo mã."""
    return DATA['CAT'].get(ma_dm)

# --- 1. Nhập liệu ---
def them_du_lieu():
    """Thêm Danh mục hoặc Sản phẩm."""
    print("\n--- CHỨC NĂNG THÊM DỮ LIỆU ---")
    print("1. Thêm Danh mục (Category)")
    print("2. Thêm Sản phẩm (Product)")
    choice = input("Chọn chức năng (1/2): ")
    
    if choice == '1':
        ma = input("Nhập Mã Danh mục: ")
        if find_cat_by_ma(ma):
            print("❌ Lỗi: Mã Danh mục đã tồn tại.")
            return
        ten = input("Nhập Tên Danh mục: ")
        DATA['CAT'][ma] = {'ten': ten}
        print(f"✅ Đã thêm Danh mục '{ten}'.")
        LuuFile()
        
    elif choice == '2':
        if not DATA['CAT']:
            print("❌ Lỗi: Cần thêm ít nhất một Danh mục trước.")
            return

        ma_dm = input("Nhập Mã Danh mục cần thêm sản phẩm vào: ")
        if not find_cat_by_ma(ma_dm):
            print("❌ Lỗi: Mã Danh mục không tồn tại.")
            return
            
        ma = input("Nhập Mã Sản phẩm: ")
        if find_product_by_ma(ma):
            print("❌ Lỗi: Mã Sản phẩm đã tồn tại.")
            return
            
        ten = input("Nhập Tên Sản phẩm: ")
        while True:
            try:
                gia = float(input("Nhập Đơn giá: "))
                break
            except ValueError:
                print("Lỗi: Đơn giá phải là số.")
                
        DATA['PROD'].append({
            'ma': ma, 
            'ten': ten, 
            'gia': gia, 
            'ma_dm': ma_dm
        })
        print(f"✅ Đã thêm Sản phẩm '{ten}'.")
        LuuFile()

# --- 2. Xuất dữ liệu ---
def xuat_danh_sach(dssp=None):
    """Xuất danh sách sản phẩm và danh mục ra màn hình."""
    
    # 1. Xuất Danh mục
    print("\n" + "=" * 50)
    print("DANH MỤC HIỆN CÓ:")
    print("-" * 50)
    if not DATA['CAT']:
        print("Danh sách Danh mục trống.")
    else:
        for ma, cat in DATA['CAT'].items():
            print(f"[{ma}] - {cat['ten']}")
    print("=" * 50)
    
    # 2. Xuất Sản phẩm
    ds_xuat = dssp if dssp is not None else DATA['PROD']
    
    print("\n" + "=" * 80)
    print("DANH SÁCH SẢN PHẨM:")
    print("-" * 80)
    print(f"| {'Mã SP':<8} | {'Tên Sản Phẩm':<30} | {'Đơn giá':<12} | {'Mã DM':<8} | {'Tên DM':<10} |")
    print("-" * 80)
    
    if not ds_xuat:
        print("| Danh sách Sản phẩm trống.                                                      |")
    else:
        for prod in ds_xuat:
            ten_dm = DATA['CAT'].get(prod['ma_dm'], {}).get('ten', 'Không rõ')
            print(f"| {prod['ma']:<8} | {prod['ten']:<30} | {prod['gia']:>12,.0f} | {prod['ma_dm']:<8} | {ten_dm:<10} |")
            
    print("=" * 80)

# --- 3. Sắp xếp ---
def sap_xep_san_pham():
    """Sắp xếp sản phẩm theo đơn giá giảm dần."""
    dssp = sorted(DATA['PROD'], key=lambda x: x['gia'], reverse=True)
    print("\n--- SẢN PHẨM SAU KHI SẮP XẾP THEO GIÁ GIẢM DẦN ---")
    xuat_danh_sach(dssp)

# --- 4. Tìm kiếm ---
def tim_kiem_san_pham():
    """Tìm kiếm sản phẩm theo tên hoặc mã."""
    keyword = input("Nhập từ khóa (Mã hoặc Tên Sản phẩm): ").lower()
    
    results = [
        prod for prod in DATA['PROD'] 
        if keyword in prod['ma'].lower() or keyword in prod['ten'].lower()
    ]
    
    if results:
        print(f"\n--- KẾT QUẢ TÌM KIẾM CHO '{keyword}' ---")
        xuat_danh_sach(results)
    else:
        print(f"❌ Không tìm thấy sản phẩm nào cho từ khóa '{keyword}'.")

# --- 5. Sửa ---
def sua_san_pham():
    """Sửa thông tin Tên và Giá của sản phẩm."""
    ma_sp = input("Nhập Mã Sản phẩm cần sửa: ")
    prod = find_product_by_ma(ma_sp)
    
    if prod:
        print(f"--- Đang sửa Sản phẩm: {prod['ten']} (Giá hiện tại: {prod['gia']}) ---")
        
        new_ten = input(f"Nhập Tên mới (Enter để giữ nguyên, hiện tại: {prod['ten']}): ")
        if new_ten:
            prod['ten'] = new_ten
            
        new_gia_str = input(f"Nhập Giá mới (Enter để giữ nguyên, hiện tại: {prod['gia']}): ")
        if new_gia_str:
            try:
                prod['gia'] = float(new_gia_str)
            except ValueError:
                print("❌ Lỗi: Giá trị nhập không hợp lệ. Giá không được thay đổi.")
                return
        
        print(f"✅ Đã cập nhật Sản phẩm '{ma_sp}'.")
        LuuFile()
    else:
        print("❌ Lỗi: Mã Sản phẩm không tồn tại.")

# --- 6. Xóa ---
def xoa_san_pham():
    """Xóa sản phẩm theo mã."""
    ma_sp = input("Nhập Mã Sản phẩm cần xóa: ")
    prod_to_delete = find_product_by_ma(ma_sp)
    
    if prod_to_delete:
        DATA['PROD'].remove(prod_to_delete)
        print(f"✅ Đã xóa Sản phẩm '{ma_sp}' thành công.")
        LuuFile()
    else:
        print("❌ Lỗi: Mã Sản phẩm không tồn tại.")

# =================================================================
# III. MENU CHÍNH
# =================================================================

def menu_chinh():
    """Hiển thị menu và xử lý lựa chọn của người dùng."""
    DocFile() # Tải dữ liệu khi khởi động
    
    while True:
        print("\n" + "#" * 30)
        print("PHẦN MỀM QUẢN LÝ SẢN PHẨM (TEXT FILE)")
        print("#" * 30)
        print("1. Thêm (Lưu mới) Danh mục/Sản phẩm")
        print("2. Sửa thông tin Sản phẩm")
        print("3. Xóa Sản phẩm")
        print("4. Xuất danh sách (Đọc File)")
        print("5. Sắp xếp Sản phẩm theo giá giảm dần")
        print("6. Tìm kiếm Sản phẩm")
        print("0. Thoát & Lưu dữ liệu")
        print("-" * 30)
        
        choice = input("Vui lòng chọn chức năng: ")
        
        if choice == '1':
            them_du_lieu()
        elif choice == '2':
            sua_san_pham()
        elif choice == '3':
            xoa_san_pham()
        elif choice == '4':
            xuat_danh_sach()
        elif choice == '5':
            sap_xep_san_pham()
        elif choice == '6':
            tim_kiem_san_pham()
        elif choice == '0':
            LuuFile() # Lưu lần cuối trước khi thoát
            print("Chương trình kết thúc. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Khởi động chương trình
if __name__ == "__main__":
    menu_chinh()