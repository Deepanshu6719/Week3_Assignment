# 1. basic mathematical approach of solution

num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# print(reverse)

# 2. convert number to string and then slicing it

num = 12345

reverse = int(str(num)[::-1])

print(reverse)


# 3.convert number to string and then looping
num = 12345
reverse = ""

for digit in str(num):
    reverse = digit + reverse

print(int(reverse))

# the best approach is the basic 1st one because  it uses only O(1) space and is good for understanding the logic
# the other converts number to string and it creates a new object and string is immutable so altering it creates a new object every time hence using extra space.