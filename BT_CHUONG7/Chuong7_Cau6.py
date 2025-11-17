import csv
import os

FILE_PATH = "data.csv"

def create_sample_csv(file_path):
    """
    Tạo file data.csv mẫu nếu nó chưa tồn tại,
    để đảm bảo chương trình có thể chạy mà không gặp lỗi File Not Found.
    """
    if not os.path.exists(file_path):
        print(f"Không tìm thấy file '{file_path}'. Đang tạo file mẫu...")
        # Dữ liệu mẫu (sử dụng dấu chấm phẩy)
        data = [
            ['ma', 'ten'],
            ['nv1', 'obama'],
            ['nv2', 'Kim Jong un'],
            ['nv3', 'Putin']
        ]
        
        try:
            # Mở file ở chế độ 'w' (write) và chỉ định delimiter là ';'
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerows(data)
            print(f"✅ Đã tạo file '{file_path}' thành công với dữ liệu mẫu.")
        except Exception as e:
            print(f"Lỗi khi tạo file mẫu: {e}")


def process_csv(file_path):
    """
    Đọc file CSV, phân tích dữ liệu bằng dấu chấm phẩy (;) và xuất ra cột 'ma' và 'ten'.
    """
    
    # Đảm bảo file tồn tại (tạo file mẫu nếu chưa có)
    create_sample_csv(file_path)
    
    # Kiểm tra lại một lần nữa sau khi cố gắng tạo
    if not os.path.exists(file_path):
        return

    print("\n" + "=" * 40)
    print("DỮ LIỆU TỪ FILE CSV (ma và ten):")
    print("=" * 40)
    print(f"| {'Mã':<5} | {'Tên':<30} |")
    print("-" * 40)

    try:
        # Mở file ở chế độ 'r' (read)
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            
            # Sử dụng csv.reader và chỉ định ký tự phân cách là ';'
            reader = csv.reader(csvfile, delimiter=';')
            
            # Bỏ qua dòng tiêu đề (Header row)
            header = next(reader, None)
            
            # Duyệt qua từng dòng dữ liệu
            for row in reader:
                
                if len(row) >= 2:
                    ma = row[0]  # Cột đầu tiên là 'ma'
                    ten = row[1] # Cột thứ hai là 'ten'
                    
                    # Xuất ra màn hình
                    print(f"| {ma:<5} | {ten:<30} |")
                else:
                    # In ra lỗi nếu dòng không đủ cột
                    print(f"| Lỗi định dạng dòng: {row}")

        print("=" * 40)

    except Exception as e:
        print(f"Đã xảy ra lỗi trong quá trình đọc file CSV: {e}")

# --- Thực thi hàm chính ---
if __name__ == "__main__":
    process_csv(FILE_PATH)