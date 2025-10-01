cases = [
    (3, 5, 7),   # (a)
    (3, 7, 5),   # (b)
    (5, 3, 7),   # (c)
    (5, 7, 3),   # (d)
    (7, 3, 5),   # (e)
    (7, 5, 3)    # (f)
]

for idx, (i, j, k) in enumerate(cases, start=1):
    # copy logic trong đề
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k

    print(f"Trường hợp {idx}: i={i}, j={j}, k={k}")


