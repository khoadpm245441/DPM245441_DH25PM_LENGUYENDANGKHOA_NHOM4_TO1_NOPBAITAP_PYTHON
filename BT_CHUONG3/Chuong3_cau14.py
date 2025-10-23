# giải bài tập chuong 3 câu 14

def dem_sao(m,n):
    dem = 0
    a = 0
    while a < m:
        b = 0
        while b < n:
            if (a * b) % 2 == 0:
                print('*', end=' ')
                dem += 1
            b += 1
        print() 
        a += 1
    return dem
so_sao = dem_sao(100, 40)     # số dấu sao là 3000
print("Số dấu * đã in ra là:", so_sao)