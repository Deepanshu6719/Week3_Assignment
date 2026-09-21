numbers = [1, 2, 3, 4, 5]

# 1. Slicing  O(n) for both time and space complexity

reverse1 = numbers[::-1]

print(reverse1)

# 2.reversed() method O(n) for both time and space complexity

reverse2 = list(reversed(numbers))

print(reverse2)

# 3.  .reverse() method O(n) time and O(1) space complexity

numbers.reverse()

print(numbers)


# 4. loop O(n) for both time and space complexity

reverse3 = []

for i in range(len(numbers) - 1, -1, -1):
    reverse3.append(numbers[i])

print(reverse3)
 
# 5. two pointer or swapping of left and right elements  O(n) time and O(1) space complexity

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print(numbers)

# for reversing the existing string and not crfeating a new string the .reverse() is best and 
# also loop approch is also using same time and space complexity so it good for understanding