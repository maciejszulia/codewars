import math


def zeros(fact):
    n = math.factorial(fact)
    s = str(n)[::-1]
    print(s)
    iteration = 0
    for digit in s:
        if digit == "0":
            iteration += 1
        else:
            break

    return iteration


print(zeros(1000))
