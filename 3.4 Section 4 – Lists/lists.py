# TODO numbers = [10, 5, 7, 2, 1]   may have different types. always numbered starting from zero.
#  TODO list is a collection of elements, but each element is a scalar.
numbers = [10, 5, 7, 2, 1]
numbers[1] = numbers[2]
numbers[0] = 100
print(numbers)
print(len(numbers))


del numbers[0]
print(numbers)
