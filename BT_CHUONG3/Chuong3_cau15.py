# giải bài tập chương 3 câu 15
'''
(a) range(5)
    tương đương range(0,5,1)
    sinh ra dãy số 0,1,2,3,4
(b) range(5, 10)
    bắt đầu từ 5, kết thúc trước 10, bước nhảy là 1
    sinh ra dãy số 5,6,7,8,9
(c) range(5, 20, 3)
    bắt đầu từ 5, kết thúc trước 20, bước nhảy là 3
    sinh ra dãy số 5,8,11,14,17
(d) range(20, 5, -1)
    bắt đầu từ 20, kết thúc sau 5, bước nhảy là -1
    sinh ra dãy số 20,19,18,17,16,15,14,13,12,11,10,9,8,7,6
(e) range(20, 5, -3)
    bắt đầu từ 20, giảm dần mỗi lần -3, kết thúc sau 5
    sinh ra dãy số 20,17,14,11,8
(f) range(10, 5)
    bắt đầu từ 10, kết thúc sau 5, bước nhảy là 1
    không thỏa điều kiện start < stop với step >0 nên kết quả rỗng
(g) range(0)
    dừng trước 0, 
    kết quả rỗng
(h) range(10, 101, 10)
    bắt đầu từ 10, kết thúc trước 101, bước nhảy là 10
    sinh ra dãy số 10,20,30,40,50,60,70,80,90,100
(i) range(10, -1, -1)
    bắt đầu từ 10, kết thúc sau -1, bước nhảy là -1
    sinh ra dãy số 10,9,8,7,6,5,4,3,2,1,0
(j) range(-3, 4)   
    bắt đầu từ -3, kết thúc trước 4, bước nhảy là 1
    sinh ra dãy số -3,-2,-1,0,1,2,3
(k) range(0, 10, 1)
    bắt đầu từ 0, kết thúc trước 10, bước nhảy là 1 
    sinh ra dãy số 0,1,2,3,4,5,6,7,8,9 
'''


'''

nếu step >0 thì dãy sẽ chạy từ start đến stop-1
nếu step <0 thì dãy sẽ chạy từ start đến stop+1
nếu điền kiện không thỏa start < stop mà step < 0 thì kết quả rỗng
'''