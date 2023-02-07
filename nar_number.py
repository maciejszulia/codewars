def narcissistic(value):
    list_of_digits = []
    for digit in str(value):
        list_of_digits.append(int(digit))
    exponent = len(list_of_digits)
    sum_of_elements = 0
    for elem in list_of_digits:
        sum_of_elements += pow(elem,exponent)
    if value == sum_of_elements:
        return True
    else:
        return False

print(narcissistic(153))
print(narcissistic(154))