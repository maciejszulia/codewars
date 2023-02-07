def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n


print(sum_of_digits(1911299999999))
print(digital_root(1911299999999))
