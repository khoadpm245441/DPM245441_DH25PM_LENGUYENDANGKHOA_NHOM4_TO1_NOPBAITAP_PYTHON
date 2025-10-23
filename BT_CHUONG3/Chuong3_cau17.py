# giải bài tập chương 3 câu 17

'''
done = False
n, m = 0, 100
while not done and n != m:
    n = int(input())
    if n < 0:
        done = True
    print("n =", n)

'''
#Viết lại
'''
n, m = 0, 100
while n <= m:
    n = int(input())
    if n<0:
        break
    print("n = ",n)
'''       