# giải bài tập chương 3 câu 5

def test_case(i,j,k):
    if i<j:
        if j<k:
            i=j
        else:
            j=k
    else:
        if j>k:
            j=i
        else:
            i=k
    print("i =",i,", j=", j, ",k= ",k)

case = [
    (3,5,7),
    (3,7,5),
    (5,3,7),
    (5,7,3),
    (7,3,5),
    (7,5,3)
]
for idx, (i,j,k) in enumerate(case, start = 1):
    print(f"Test case {idx}: ban dau i={i}, j={j}, k={k}")
    test_case(i,j,k)
    print("_" * 40)

