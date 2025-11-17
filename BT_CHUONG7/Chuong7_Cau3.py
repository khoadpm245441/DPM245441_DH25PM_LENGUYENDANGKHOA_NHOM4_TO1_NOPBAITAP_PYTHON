from xml.dom import minidom
import os

FILE_PATH = "employees.xml"

# --- Hàm đọc và xử lý XML bằng DOM ---
def read_xml_dom(file_path):
    """
    Đọc dữ liệu từ file XML bằng DOM và in ra màn hình.
    """
    
    # Kiểm tra sự tồn tại của file trước khi cố gắng đọc
    if not os.path.exists(file_path):
        print(f"LỖI: Không tìm thấy file '{file_path}'. Vui lòng đảm bảo file đã được tạo và nằm cùng thư mục.")
        # Tạo nội dung file mẫu nếu chưa có để người dùng tiện kiểm tra
        print("\n--- Gợi ý: Nội dung cần có trong employees.xml ---")
        print("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>")
        print("<employees>")
        print("    <employee><id>1</id><name>Trần Duy Thanh</name></employee>")
        print("    <employee><id>2</id><name>Lê Hoành Sử</name></employee>")
        print("</employees>")
        return

    try:
        # 1. Phân tích cú pháp XML để tạo cây DOM
        doc = minidom.parse(file_path)
        
        # 2. Lấy danh sách các phần tử (Node) <employee>
        employees = doc.getElementsByTagName('employee')
        
        print("=" * 40)
        print("DANH SÁCH NHÂN VIÊN (Đọc bằng XML DOM)")
        print("=" * 40)
        
        # 3. Duyệt qua từng phần tử <employee> và lấy dữ liệu
        for employee in employees:
            
            # Hàm phụ để lấy giá trị văn bản của thẻ con
            def get_text_by_tag_name(element, tag_name):
                # Lấy node đầu tiên có tên tag_name
                nodes = element.getElementsByTagName(tag_name)
                if nodes and nodes[0].firstChild:
                    # Lấy dữ liệu của TextNode bên trong
                    return nodes[0].firstChild.data
                return "N/A"

            emp_id = get_text_by_tag_name(employee, 'id')
            emp_name = get_text_by_tag_name(employee, 'name')
            
            # 4. Xuất dữ liệu ra màn hình
            print(f"| ID: {emp_id:<5} | Tên: {emp_name}")
            print("-" * 40)

    except Exception as e:
        print(f"Đã xảy ra lỗi khi xử lý file XML. Vui lòng kiểm tra lại cấu trúc file: {e}")

# --- Logic chính ---
if __name__ == "__main__":
    read_xml_dom(FILE_PATH)