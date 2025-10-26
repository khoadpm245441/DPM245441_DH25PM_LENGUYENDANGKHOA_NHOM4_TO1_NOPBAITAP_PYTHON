def ToiUuChuoi(s):
    s2 = s.strip()          # Bỏ khoảng trắng đầu và cuối chuỗi
    arr = s2.split(' ')     # Tách các từ theo dấu cách
    s2 = ""                 # Tạo chuỗi rỗng để ghép từ lại

    for x in arr:
        word = x
        if len(word.strip()) != 0:   # Nếu từ không rỗng
            s2 += word + " "
    return s2.strip()       # Trả về chuỗi sau khi bỏ khoảng trắng dư

# --- Chương trình chính ---
s = "   Trần    Duy   Thanh   "
print("Trước khi tối ưu:", s, "=> độ dài =", len(s))

s = ToiUuChuoi(s)
print("Sau khi tối ưu:  ", s, "=> độ dài =", len(s))
