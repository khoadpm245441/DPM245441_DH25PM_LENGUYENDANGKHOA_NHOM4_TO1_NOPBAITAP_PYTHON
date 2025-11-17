import json
import os

FILE_PATH = "student_management.json"
# Cấu trúc dữ liệu trong bộ nhớ: Dictionary với Mã Lớp là key
DATA = {} 

# =================================================================
# I. CHỨC NĂNG XỬ LÝ FILE (ĐỌC & GHI JSON)
# =================================================================

def DocFile():
    """Đọc dữ liệu từ file JSON và tải vào biến DATA trong bộ nhớ."""
    global DATA
    if not os.path.exists(FILE_PATH):
        DATA = {}
        return
    
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            # Sử dụng json.load() để chuyển JSON thành Python Object (Dictionary)
            DATA = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        DATA = {}
    except Exception as e:
        print(f"Lỗi khi đọc file JSON: {e}")
        DATA = {}

def LuuFile():
    """Lưu dữ liệu từ bộ nhớ (biến DATA) ra file JSON."""
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            # Sử dụng json.dump() để chuyển Python Object thành JSON String
            # indent=4 và ensure_ascii=False để file dễ đọc (pretty print) và hỗ trợ tiếng Việt
            json.dump(DATA, file, indent=4, ensure_ascii=False)
        print(f"\n✅ Đã lưu dữ liệu thành công vào file '{FILE_PATH}'.")
    except Exception as e:
        print(f"Lỗi khi lưu file JSON: {e}")

# =================================================================
# II. CÁC HÀM TIỆN ÍCH
# =================================================================

def find_student_by_ma(ma_sv):
    """Tìm kiếm sinh viên theo mã (trong tất cả các lớp)."""
    for ma_lop, lop in DATA.items():
        for sv in lop.get('sinh_vien', []):
            if sv['ma'] == ma_sv:
                return sv, ma_lop # Trả về sinh viên và mã lớp chứa sinh viên đó
    return None, None

def find_class_by_ma(ma_lop):
    """Tìm kiếm lớp theo mã."""
    return DATA.get(ma_lop)

# =================================================================
# III. CHỨC NĂNG XỬ LÝ DỮ LIỆU (CRUD)
# =================================================================

# --- 1. Nhập liệu (Thêm) ---
def them_du_lieu():
    """Thêm Lớp hoặc Sinh viên."""
    print("\n--- CHỨC NĂNG THÊM DỮ LIỆU ---")
    print("1. Thêm Lớp")
    print("2. Thêm Sinh viên")
    choice = input("Chọn chức năng (1/2): ")
    
    if choice == '1':
        ma = input("Nhập Mã Lớp: ").upper()
        if find_class_by_ma(ma):
            print("❌ Lỗi: Mã Lớp đã tồn tại.")
            return
        ten = input("Nhập Tên Lớp: ")
        DATA[ma] = {'ten_lop': ten, 'sinh_vien': []}
        print(f"✅ Đã thêm Lớp '{ten}'.")
        LuuFile()
        
    elif choice == '2':
        if not DATA:
            print("❌ Lỗi: Cần thêm ít nhất một Lớp trước.")
            return

        ma_lop = input("Nhập Mã Lớp cần thêm sinh viên vào: ").upper()
        lop = find_class_by_ma(ma_lop)
        if not lop:
            print("❌ Lỗi: Mã Lớp không tồn tại.")
            return
            
        ma_sv = input("Nhập Mã Sinh viên: ")
        if find_student_by_ma(ma_sv)[0]:
            print("❌ Lỗi: Mã Sinh viên đã tồn tại.")
            return
            
        ten_sv = input("Nhập Tên Sinh viên: ")
        while True:
            try:
                nam_sinh = int(input("Nhập Năm sinh: "))
                break
            except ValueError:
                print("Lỗi: Năm sinh phải là số nguyên.")
                
        lop['sinh_vien'].append({
            'ma': ma_sv, 
            'ten': ten_sv, 
            'nam_sinh': nam_sinh
        })
        print(f"✅ Đã thêm Sinh viên '{ten_sv}' vào Lớp '{lop['ten_lop']}'.")
        LuuFile()

# --- 2. Xuất dữ liệu (Đọc File) ---
def xuat_danh_sach(ds_sv_output=None):
    """Xuất danh sách Lớp và Sinh viên ra màn hình."""
    
    print("\n" + "=" * 80)
    print("DANH SÁCH LỚP HỌC VÀ SINH VIÊN:")
    print("=" * 80)

    # Nếu đang xuất kết quả tìm kiếm/sắp xếp (dạng flat list), dùng ds_sv_output
    if ds_sv_output is not None:
        print("KẾT QUẢ XUẤT/SẮP XẾP:")
        ds_sv = ds_sv_output
    else:
        # Nếu xuất toàn bộ (dạng phân cấp), gom tất cả sinh viên lại
        ds_sv = []
        for ma_lop, lop in DATA.items():
            for sv in lop.get('sinh_vien', []):
                # Thêm thông tin lớp vào để hiển thị
                sv_info = sv.copy() 
                sv_info['ma_lop'] = ma_lop
                sv_info['ten_lop'] = lop['ten_lop']
                ds_sv.append(sv_info)
    
    if not ds_sv:
        print("Danh sách Sinh viên trống.")
        return
        
    print(f"| {'Mã SV':<8} | {'Tên Sinh viên':<25} | {'Năm sinh':<10} | {'Mã Lớp':<8} | {'Tên Lớp':<20} |")
    print("-" * 80)
    
    for sv in ds_sv:
        print(f"| {sv['ma']:<8} | {sv['ten']:<25} | {sv['nam_sinh']:<10} | {sv['ma_lop']:<8} | {sv['ten_lop']:<20} |")
            
    print("=" * 80)

# --- 3. Sắp xếp ---
def sap_xep_sinh_vien():
    """Sắp xếp sinh viên theo Năm sinh giảm dần."""
    # Gom tất cả sinh viên lại thành một list phẳng
    all_students = []
    for ma_lop, lop in DATA.items():
        for sv in lop.get('sinh_vien', []):
            sv_info = sv.copy()
            sv_info['ma_lop'] = ma_lop
            sv_info['ten_lop'] = lop['ten_lop']
            all_students.append(sv_info)
            
    # Sắp xếp theo 'nam_sinh' (giảm dần)
    ds_sv_sorted = sorted(all_students, key=lambda x: x['nam_sinh'], reverse=True)
    
    print("\n--- SINH VIÊN SAU KHI SẮP XẾP THEO NĂM SINH GIẢM DẦN ---")
    xuat_danh_sach(ds_sv_sorted)

# --- 4. Tìm kiếm ---
def tim_kiem_sinh_vien():
    """Tìm kiếm sinh viên theo tên hoặc mã."""
    keyword = input("Nhập từ khóa (Mã hoặc Tên Sinh viên): ").lower()
    
    results = []
    for ma_lop, lop in DATA.items():
        for sv in lop.get('sinh_vien', []):
            if keyword in sv['ma'].lower() or keyword in sv['ten'].lower():
                sv_info = sv.copy()
                sv_info['ma_lop'] = ma_lop
                sv_info['ten_lop'] = lop['ten_lop']
                results.append(sv_info)

    if results:
        print(f"\n--- KẾT QUẢ TÌM KIẾM CHO '{keyword}' ---")
        xuat_danh_sach(results)
    else:
        print(f"❌ Không tìm thấy sinh viên nào cho từ khóa '{keyword}'.")

# --- 5. Sửa ---
def sua_sinh_vien():
    """Sửa thông tin Tên và Năm sinh của sinh viên."""
    ma_sv = input("Nhập Mã Sinh viên cần sửa: ")
    prod, ma_lop = find_student_by_ma(ma_sv)
    
    if prod:
        print(f"--- Đang sửa SV: {prod['ten']} (Năm sinh hiện tại: {prod['nam_sinh']}) ---")
        
        new_ten = input(f"Nhập Tên mới (Enter để giữ nguyên, hiện tại: {prod['ten']}): ")
        if new_ten:
            prod['ten'] = new_ten
            
        new_nam_sinh_str = input(f"Nhập Năm sinh mới (Enter để giữ nguyên, hiện tại: {prod['nam_sinh']}): ")
        if new_nam_sinh_str:
            try:
                prod['nam_sinh'] = int(new_nam_sinh_str)
            except ValueError:
                print("❌ Lỗi: Giá trị Năm sinh không hợp lệ. Năm sinh không được thay đổi.")
                return
        
        print(f"✅ Đã cập nhật Sinh viên '{ma_sv}'.")
        LuuFile()
    else:
        print("❌ Lỗi: Mã Sinh viên không tồn tại.")

# --- 6. Xóa ---
def xoa_sinh_vien():
    """Xóa sinh viên theo mã."""
    ma_sv = input("Nhập Mã Sinh viên cần xóa: ")
    sv_to_delete, ma_lop = find_student_by_ma(ma_sv)
    
    if sv_to_delete:
        # Xóa sinh viên khỏi list sinh_vien của lớp tương ứng
        DATA[ma_lop]['sinh_vien'].remove(sv_to_delete)
        print(f"✅ Đã xóa Sinh viên '{ma_sv}' khỏi Lớp '{ma_lop}' thành công.")
        
        # Tùy chọn: Xóa luôn lớp nếu không còn sinh viên nào
        if not DATA[ma_lop]['sinh_vien']:
             del DATA[ma_lop]
             print(f"⚠️ Lớp '{ma_lop}' không còn sinh viên, đã xóa lớp.")
             
        LuuFile()
    else:
        print("❌ Lỗi: Mã Sinh viên không tồn tại.")

# =================================================================
# IV. MENU CHÍNH
# =================================================================

def menu_chinh():
    """Hiển thị menu và xử lý lựa chọn của người dùng."""
    DocFile() # Tải dữ liệu khi khởi động
    
    while True:
        print("\n" + "#" * 30)
        print("PHẦN MỀM QUẢN LÝ SINH VIÊN (JSON FILE)")
        print("#" * 30)
        print("1. Thêm (Lưu mới) Lớp/Sinh viên")
        print("2. Sửa thông tin Sinh viên")
        print("3. Xóa Sinh viên")
        print("4. Xuất danh sách (Đọc File)")
        print("5. Sắp xếp Sinh viên theo Năm sinh giảm dần")
        print("6. Tìm kiếm Sinh viên")
        print("0. Thoát & Lưu dữ liệu")
        print("-" * 30)
        
        choice = input("Vui lòng chọn chức năng: ")
        
        if choice == '1':
            them_du_lieu()
        elif choice == '2':
            sua_sinh_vien()
        elif choice == '3':
            xoa_sinh_vien()
        elif choice == '4':
            xuat_danh_sach()
        elif choice == '5':
            sap_xep_sinh_vien()
        elif choice == '6':
            tim_kiem_sinh_vien()
        elif choice == '0':
            LuuFile() # Lưu lần cuối trước khi thoát
            print("Chương trình kết thúc. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Khởi động chương trình
if __name__ == "__main__":
    menu_chinh()