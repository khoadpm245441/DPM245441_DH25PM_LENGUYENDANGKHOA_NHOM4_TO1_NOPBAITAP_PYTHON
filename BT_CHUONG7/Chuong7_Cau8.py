import openpyxl
import os

FILE_PATH = "demo.xlsx"

def read_excel_file(file_path):
    """
    Sử dụng openpyxl để đọc file demo.xlsx và xuất dữ liệu ra màn hình.
    """
    if not os.path.exists(file_path):
        print(f"LỖI: Không tìm thấy file '{file_path}'. Vui lòng chạy Câu 7 để tạo file.")
        return

    try:
        # 1. Tải Workbook
        workbook = openpyxl.load_workbook(file_path)
        
        # 2. Chọn Worksheet đầu tiên
        # Hoặc dùng worksheet = workbook['Tên Sheet'] nếu bạn biết tên
        sheet = workbook.active
        
        print("=" * 60)
        print(f"DỮ LIỆU ĐỌC TỪ FILE EXCEL: {file_path}")
        print("=" * 60)
        
        # 3. Duyệt qua từng hàng trong sheet
        
        # Lấy tiêu đề và in
        header_row = [cell.value for cell in sheet[1]]
        print(f"| {header_row[0]:<5} | {header_row[1]:<15} | {header_row[2]:<20} | {header_row[3]:<10} | {header_row[4]:<10} |")
        print("-" * 60)
        
        # Bắt đầu đọc từ hàng thứ 2 (chỉ số 2) - là hàng dữ liệu
        for row in sheet.iter_rows(min_row=2, values_only=True):
            # row là một tuple chứa giá trị của các ô
            
            # Kiểm tra và xử lý dữ liệu để in ra (chuyển float thành int cho đẹp)
            stt = row[0] if row[0] is not None else ""
            ma_sp = row[1] if row[1] is not None else ""
            ten_sp = row[2] if row[2] is not None else ""
            so_luong = int(row[3]) if isinstance(row[3], (int, float)) else ""
            don_gia = int(row[4]) if isinstance(row[4], (int, float)) else ""
            
            print(f"| {stt:<5} | {ma_sp:<15} | {ten_sp:<20} | {so_luong:<10} | {don_gia:<10} |")
            
        print("=" * 60)

    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file Excel: {e}")

# --- Thực thi hàm chính ---
if __name__ == "__main__":
    read_excel_file(FILE_PATH)