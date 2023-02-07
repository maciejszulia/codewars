arr = [19, 5, 42, 2, 77]

def sum_two_smallest_numbers(numbers):
    smallest = min(numbers)
    numbers.remove(smallest)
    second_smallest = min(numbers)
    return smallest + second_smallest
    #your code here

print(sum_two_smallest_numbers(arr))