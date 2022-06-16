def get_ith_bit(number, i):
    mask = 1 << i
    return 1 if (number & mask) > 0 else 0

def clear_ith_bit(number, i):
    mask = ~(1 << i)
    return number & mask



x = get_ith_bit(5, 2)
print(x)