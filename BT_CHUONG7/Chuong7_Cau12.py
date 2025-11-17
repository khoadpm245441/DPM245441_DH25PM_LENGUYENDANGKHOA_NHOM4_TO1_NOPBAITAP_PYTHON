import csv
import random
import os

FILE_PATH = "random_numbers.csv"
NUM_ROWS = 10
NUM_COLS = 10
DELIMITER = ';'

# =================================================================
# I. CHỨC NĂNG TẠO FILE CSV
# =================================================================

def create_random_csv(file_path):
    """
    Tạo file CSV với 10 dòng, mỗi dòng 10 số ngẫu nhiên (1-99) cách nhau bởi ';'.
    """
    print(f"\n--- 1. TẠO FILE '{file_path}' ---")
    data_to_write = []
    
    # Tạo 10 dòng dữ liệu
    for i in range(NUM_ROWS):
        # Tạo 10 số ngẫu nhiên từ 1 đến 99
        row = [random.randint(1, 99) for _ in range(NUM_COLS)]
        data_to_write.append(row)
        
    try:
        # Ghi dữ liệu vào file
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=DELIMITER)
            writer.writerows(data_to_write)
        print(f"✅ Đã tạo file '{file_path}' thành công với {NUM_ROWS}x{NUM_COLS} số ngẫu nhiên.")
    except Exception as e:
        print(f"❌ Lỗi khi tạo file CSV: {e}")


# =================================================================
# II. CHỨC NĂNG ĐỌC FILE VÀ TÍNH TỔNG
# =================================================================

def read_and_sum_csv(file_path):
    """
    Đọc file CSV, tính tổng các số trên mỗi dòng và xuất ra màn hình.
    """
    print(f"\n--- 2. ĐỌC VÀ TÍNH TỔNG DỮ LIỆU TỪ FILE '{file_path}' ---")
    if not os.path.exists(file_path):
        print(f"❌ Lỗi: Không tìm thấy file '{file_path}'. Vui lòng tạo file trước.")
        return

    print("=" * 60)
    print(f"| {'Dữ liệu dòng':<40} | {'Tổng':<15} |")
    print("-" * 60)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=DELIMITER)
            
            for row in reader:
                current_sum = 0
                valid_numbers = []
                
                # Duyệt qua từng phần tử trong dòng
                for item in row:
                    try:
                        # Chuyển đổi sang số nguyên và cộng dồn
                        number = int(item.strip())
                        current_sum += number
                        valid_numbers.append(str(number))
                    except ValueError:
                        # Bỏ qua nếu không phải là số
                        continue
                
                # Xuất ra màn hình
                row_str = DELIMITER.join(valid_numbers)
                print(f"| {row_str:<40} | {current_sum:<15} |")

        print("=" * 60)

    except Exception as e:
        print(f"❌ Đã xảy ra lỗi trong quá trình đọc file: {e}")

# =================================================================
# III. CHẠY CHƯƠNG TRÌNH
# =================================================================

if __name__ == "__main__":
    create_random_csv(FILE_PATH)
    read_and_sum_csv(FILE_PATH)