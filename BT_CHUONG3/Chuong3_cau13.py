# giải bài tập chương 3 câu 13

def dem_dau_sao(n):
    dem = 0
    a = 0
    while a < n:
        print('*', end=' ')
        dem += 1
        a += 1
    print() 
    return dem

so_sao = dem_dau_sao(201)
print("Số dấu * đã in ra là:", so_sao)