def horner_new(a, x, n):
    if n == 0:
        return a[0]
    else:
        return x * horner_new(a, x, n-1) + a[n]

# So sánh kết quả với hàm Horner
def horner(a, x, n):
    p = a[n]
    for i in range(n-1, -1, -1):
        p = p * x + a[i]
    return p

# Test các trường hợp đã cho
a1 = [1, 3, 5, 4]
x1 = 2
n1 = 3
a2 = [2, -3, -1, 9, 4, -7]
x2 = 3
n2 = 5

# Kết quả từ hàm Horner
result1 = horner(a1, x1, n1)
result2 = horner(a2, x2, n2)

# Kết quả từ hàm đệ quy Horner_new
result1_new = horner_new(a1, x1, n1)
result2_new = horner_new(a2, x2, n2)

print(result1, result2, result1_new, result2_new)

