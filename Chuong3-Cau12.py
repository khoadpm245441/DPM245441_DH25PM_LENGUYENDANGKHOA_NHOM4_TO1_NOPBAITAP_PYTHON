print("Bảng cửu chương từ 2 đến 9:\n")

for i in range(1, 11):      # i chạy từ 1 đến 10
    for j in range(2, 10):  # j chạy từ 2 đến 9
        line = "{0} * {1:>2} = {2:>2}".format(j, i, i*j)
        print(line, end="\t")   # in cùng dòng, cách nhau tab
    print()   # xuống dòng sau khi in xong 1 hàng
