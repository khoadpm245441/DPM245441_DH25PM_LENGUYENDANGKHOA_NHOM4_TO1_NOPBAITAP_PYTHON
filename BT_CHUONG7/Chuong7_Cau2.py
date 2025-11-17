FILE_PATH = "data_cau2.txt"

def DocVaXuLyFile(path):
    """
    Thực hiện chức năng a) và b) trên nội dung của file.
    path: Tên hoặc đường dẫn đến file dữ liệu.
    """
    
    # 1. Khởi tạo danh sách để lưu dữ liệu của toàn bộ file
    data_list_of_lists = []
    
    print("=" * 50)
    print("a) ĐỌC FILE, KHỞI TẠO LIST VÀ XUẤT RA MÀN HÌNH:")
    print("=" * 50)

    try:
        with open(path, 'r', encoding='utf-8') as file:
            line_number = 1
            for line in file:
                # Loại bỏ khoảng trắng/ký tự xuống dòng ở đầu/cuối
                raw_data = line.strip()
                
                if not raw_data: # Bỏ qua dòng trống
                    continue
                
                # Tách chuỗi thành các phần tử (dạng chuỗi)
                string_list = raw_data.split(',')
                
                # Chuyển đổi các phần tử từ chuỗi sang số nguyên (int)
                # Dùng list comprehension để chuyển đổi hiệu quả
                try:
                    number_list = [int(item) for item in string_list]
                    data_list_of_lists.append(number_list)
                    
                    # Xuất list vừa tạo ra màn hình (Chức năng a)
                    print(f"Dòng {line_number} (List): {number_list}")
                    
                    # --- Bắt đầu Chức năng b) ---
                    # Lọc các số âm
                    negative_numbers = [num for num in number_list if num < 0]
                    
                    # Xuất các số âm trên mỗi dòng ra màn hình (Chức năng b)
                    if negative_numbers:
                        print(f"   -> Các số âm: {negative_numbers}")
                    else:
                        print("   -> Không có số âm.")
                        
                    line_number += 1
                    
                except ValueError:
                    print(f"Lỗi: Dòng {line_number} chứa ký tự không phải số. Bỏ qua dòng này.")
                    line_number += 1
                    continue
                    
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file '{path}'. Vui lòng kiểm tra lại tên file và đường dẫn.")
        return

    print("=" * 50)
    print("\nKết thúc quá trình xử lý file.")
    # Có thể trả về data_list_of_lists nếu cần xử lý tiếp
    # return data_list_of_lists 

# Thực thi hàm chính
if __name__ == "__main__":
    DocVaXuLyFile(FILE_PATH)