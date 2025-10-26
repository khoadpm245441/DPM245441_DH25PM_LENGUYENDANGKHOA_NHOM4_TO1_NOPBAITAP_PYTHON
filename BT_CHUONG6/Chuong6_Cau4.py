# Câu 4: Xác định kết quả khi thực thi list

lst = [3, 0, 1, 5, 2]
x = 2

print("lst =", lst)
print("x =", x)
print()

print("(a) lst[0] =", lst[0])
print("(b) lst[3] =", lst[3])
print("(c) lst[x] =", lst[x])
print("(d) lst[-x] =", lst[-x])
print("(e) lst[x + 1] =", lst[x + 1])
print("(f) lst[x] + 1 =", lst[x] + 1)
print("(g) lst[lst[x]] =", lst[lst[x]])
print("(h) lst[lst[lst[x]]] =", lst[lst[lst[x]]])

'''
lst = [3, 0, 1, 5, 2]
x = 2

(a) lst[0] = 3
(b) lst[3] = 5
(c) lst[x] = 1
(d) lst[-x] = 5
(e) lst[x + 1] = 5
(f) lst[x] + 1 = 2
(g) lst[lst[x]] = 0
(h) lst[lst[lst[x]]] = 3
'''