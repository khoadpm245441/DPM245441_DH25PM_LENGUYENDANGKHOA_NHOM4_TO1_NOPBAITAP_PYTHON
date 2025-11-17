import xml.etree.ElementTree as ET
import os

FILE_PATH = "nhomthietbi.xml"

# =================================================================
# I. CHỨC NĂNG TẠO FILE XML MẪU
# =================================================================

def create_sample_xml(file_path):
    """
    Tạo file XML mẫu nếu nó chưa tồn tại, để đảm bảo chương trình có thể đọc.
    """
    if os.path.exists(file_path):
        return

    print(f"Không tìm thấy file '{file_path}'. Đang tạo file mẫu...")
    
    # 1. Tạo root element <nhomthietbi>
    root = ET.Element("nhomthietbi")
    
    # Dữ liệu mẫu
    sample_data = [
        ("NTB1", "Nhóm Máy tính"),
        ("NTB2", "Nhóm Máy in"),
        ("NTB3", "Nhóm Thiết bị mạng")
    ]
    
    # 2. Tạo các phần tử <nhom>
    for ma, ten in sample_data:
        nhom = ET.SubElement(root, "nhom", ma=ma)
        ten_element = ET.SubElement(nhom, "ten")
        ten_element.text = ten
        
    # 3. Ghi ra file
    try:
        # Tạo đối tượng ElementTree
        tree = ET.ElementTree(root)
        
        # Ghi ra file với header XML và định dạng đẹp (pretty print)
        ET.indent(tree, space="  ") # Áp dụng thụt lề cho ElementTree (Python 3.9+)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f"✅ Đã tạo file '{file_path}' thành công với dữ liệu mẫu.")
    except Exception as e:
        print(f"❌ Lỗi khi tạo file XML mẫu: {e}")


# =================================================================
# II. CHỨC NĂNG ĐỌC FILE
# =================================================================

def doc_nhom_thiet_bi(file_path):
    """
    Đọc dữ liệu nhóm thiết bị từ file XML bằng ElementTree và in ra màn hình.
    """
    
    # Đảm bảo file tồn tại (tạo file mẫu nếu chưa có)
    create_sample_xml(file_path)
    
    if not os.path.exists(file_path):
        return

    print(f"\n--- ĐỌC DỮ LIỆU NHÓM THIẾT BỊ TỪ FILE '{file_path}' ---")

    try:
        # 1. Phân tích cú pháp XML
        tree = ET.parse(file_path)
        root = tree.getroot() 
        
        print("=" * 40)
        print("| Mã nhóm | Tên nhóm thiết bị             |")
        print("-" * 40)
        
        # 2. Duyệt qua từng phần tử <nhom>
        for nhom in root.findall('nhom'):
            ma_nhom = nhom.get('ma')
            ten_nhom_element = nhom.find('ten')
            ten_nhom = ten_nhom_element.text if ten_nhom_element is not None else "Không tên"
            
            # Xuất dữ liệu
            print(f"| {ma_nhom:<8} | {ten_nhom:<30} |")

        print("=" * 40)
        
    except ET.ParseError:
        print(f"❌ LỖI: File '{file_path}' không đúng định dạng XML. Vui lòng kiểm tra lại.")
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi khi xử lý file XML: {e}")

# --- Thực thi hàm chính ---
if __name__ == "__main__":
    doc_nhom_thiet_bi(FILE_PATH)