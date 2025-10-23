# giải bài tập chương 3 câu 18

def hinh1(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def hinh2(n):
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
def hinh3(n):
    for i in range(n):
        for j in range(n):
            if i == n//2 or j == n//2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


n=5
print("hinh 1: ")
hinh1(n)
print("\nhinh 2: ")
hinh2(n)
print("\nhinh 3: ")
hinh3(n)



