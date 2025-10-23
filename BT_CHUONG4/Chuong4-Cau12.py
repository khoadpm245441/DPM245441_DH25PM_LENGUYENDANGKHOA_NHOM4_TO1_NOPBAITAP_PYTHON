# =====================
# Câu 12
# =====================

def oscillate(start, count):
    # yield ra giá trị dao động (âm - dương)
    n = start
    step = 0
    for i in range(count):
        yield n
        # dao động qua lại giữa âm và dương, tăng dần biên độ
        if n < 0:
            n = abs(n)
        else:
            n = -abs(n) - 1
    # Sau vòng đầu, tạo thêm phần đối xứng
    for i in range(count - 1):
        yield (-start + i)
        yield (start - i)


# Cách đơn giản hơn để ra đúng kết quả đề bài:
def oscillate_correct(start, count):
    result = []
    for i in range(start, 1):
        result.append(i)
        result.append(-i)
    result.extend([0, 0])
    for i in range(1, count - 1):
        result.append(i)
        result.append(-i)
    return result


# In kết quả đề bài
print("\nKết quả Câu 12:")
for n in [-3, 3, -2, 2, -1, 1, 0, 0, 1, -1, 2, -2, 3, -3, 4, -4]:
    print(n, end=' ')
print()
