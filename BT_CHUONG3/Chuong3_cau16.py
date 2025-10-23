# giải bài tập chuong 3 câu 16

def dem_sao():
    dem = 0
    for a in range(20, 101, 5):
        print('*', end=' ')
        dem += 1
    print()
    return dem
so_sao = dem_sao()     # số dấu sao là 17
print("Số dấu * đã in ra là:", so_sao)