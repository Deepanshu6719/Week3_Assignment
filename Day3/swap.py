numbers = [10, 20, 30, 40, 50]

# 1. unpacking , best as no extar variables and sapce required simple and effective

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

# 2. temp variable
temp = numbers[0]

numbers[0] = numbers[-1]
numbers[-1] = temp

print(numbers)

# 3. slicing
numbers[0:1], numbers[-1:] = numbers[-1:], numbers[0:1]

print(numbers)