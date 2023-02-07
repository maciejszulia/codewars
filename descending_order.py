def descending_order(num):
    number_to_string = str(num)
    list_of_digits = [str(digit) for digit in number_to_string]
    list_of_digits.sort(reverse=True)
    output = "".join(list_of_digits)
    return int(output)

print(descending_order(31122))