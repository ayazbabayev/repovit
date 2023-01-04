def get_real_floor(n):
    if n < 0:
        return n
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif 13 >= n > 1:
        return n-1
    elif n >= 14:
        return n-2
n = 15

print(get_real_floor(n))
