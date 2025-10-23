# giải bài tập chương 3 câu 6

def doc_chu_so_hang_don_vi(so):
    chu_so = {
        0: "không",
        1: "một",
        2: "hai",
        3: "ba",
        4: "bốn",
        5: "năm",
        6: "sáu",
        7: "bảy",
        8: "tám",
        9: "chín"
    }
    return chu_so.get(so, "")
def doc_so(so):
    if so < 0 or so > 99:
        return "chỉ nhập trong khoảng từ 0 đến 99."
    
    if so < 10:
        if so == 0:
            return "không"
        return doc_chu_so_hang_don_vi(so)

    chuc = so // 10
    dv = so % 10

    ket_qua = ""
    if chuc == 1:
        ket_qua += "mười"
    else:
        ket_qua += doc_chu_so_hang_don_vi(chuc) + " mươi"

    if dv == 0:
        return ket_qua 
    elif dv == 1:
        if chuc >= 1:  
            ket_qua += " mốt"
        else:
            ket_qua += " một"
    elif dv == 4:
        ket_qua += " tư"
    elif dv == 5:
        ket_qua += " lăm"   
    else:
        ket_qua += " " + doc_chu_so_hang_don_vi(dv)
    return ket_qua.strip()
def main():
    n = int(input("Nhập số nguyên n (0 <= n <= 99): "))
    print(f"Số {n} đọc là: {doc_so(n)}")   

if __name__ == "__main__":
    main()