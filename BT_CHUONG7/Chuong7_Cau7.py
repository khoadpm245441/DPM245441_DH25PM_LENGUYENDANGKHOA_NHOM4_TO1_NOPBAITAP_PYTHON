import xlsxwriter
import os

def create_excel_file():
    """Tạo file Excel 'demo.xlsx' với cấu trúc và dữ liệu sản phẩm."""
    
    # 1. Định nghĩa tên file và dữ liệu
    file_name = 'demo.xlsx'
    
    # Dữ liệu sản phẩm (không bao gồm tiêu đề)
    data = [
        ['1', 'SP1', 'Coca', 15, 15000],
        ['2', 'SP2', 'Pepsi', 20, 18000],
    ]
    
    # Tiêu đề cột
    headers = ['STT', 'MÃ SẢN PHẨM', 'TÊN SẢN PHẨM', 'SỐ LƯỢNG', 'ĐƠN GIÁ']
    
    # Vị trí bắt đầu ghi dữ liệu (ví dụ: A2)
    start_row = 1 
    start_col = 0 # Cột A
    
    # 2. Tạo Workbook và Worksheet
    try:
        workbook = xlsxwriter.Workbook(file_name)
        # Tên Sheet có thể thay đổi
        worksheet = workbook.add_worksheet('Sheet1') 
    except Exception as e:
        print(f"Lỗi khi tạo Workbook: {e}")
        return

    # 3. Định dạng (Format)
    
    # Định dạng tiêu đề (In đậm, Căn giữa)
    header_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1 # Thêm viền nếu cần
    })
    
    # Định dạng căn lề chung cho dữ liệu
    data_format = workbook.add_format({'align': 'left'})
    
    # Định dạng số cho Đơn giá (ví dụ: không dấu phẩy)
    price_format = workbook.add_format({'num_format': '#,##0'}) # Có thể dùng '0' hoặc '#,##0'

    # 4. Thiết lập độ rộng cột (tùy chọn, để file dễ nhìn hơn)
    worksheet.set_column('A:A', 5)  # STT
    worksheet.set_column('B:B', 15) # MÃ SẢN PHẨM
    worksheet.set_column('C:C', 20) # TÊN SẢN PHẨM
    worksheet.set_column('D:D', 10) # SỐ LƯỢNG
    worksheet.set_column('E:E', 15) # ĐƠN GIÁ

    # 5. Ghi Tiêu đề cột (Header)
    # Ghi từ ô A1 (start_row=0, start_col=0)
    for col_num, value in enumerate(headers):
        worksheet.write(start_row - 1, col_num, value, header_format)
        
    # 6. Ghi Dữ liệu (Data)
    row_num = start_row # Bắt đầu từ hàng 2 trong Excel (chỉ số 1)
    for row_data in data:
        # Ghi STT, Mã, Tên, Số lượng (dùng data_format)
        worksheet.write(row_num, 0, row_data[0], data_format) # STT
        worksheet.write(row_num, 1, row_data[1], data_format) # Mã SP
        worksheet.write(row_num, 2, row_data[2], data_format) # Tên SP
        worksheet.write(row_num, 3, row_data[3], data_format) # Số lượng
        
        # Ghi Đơn giá (dùng price_format)
        worksheet.write(row_num, 4, row_data[4], price_format) # Đơn giá

        row_num += 1

    # 7. Đóng Workbook
    try:
        workbook.close()
        print(f"✅ Đã tạo file Excel '{file_name}' thành công.")
        print(f"File được lưu tại: {os.path.abspath(file_name)}")
    except xlsxwriter.exceptions.FileCreateError:
        print(f"LỖI: Không thể lưu file '{file_name}'. Vui lòng đóng file Excel nếu nó đang mở và thử lại.")
    except Exception as e:
        print(f"Lỗi khi đóng Workbook: {e}")

# --- Thực thi hàm chính ---
if __name__ == "__main__":
    create_excel_file()