s = "Deepanshu Gupta"

# 1. loop and in for checking vowels present (matching)

count1 = 0

for char in s:
    if char.lower() in "aeiou":
        count1 += 1

print(count1)

# 2. Set, uses extra space as set is storing vowels for comparison
vowels = {"a", "e", "i", "o", "u"}

count2 = 0

for char in s.lower():
    if char in vowels:
        count2 += 1

print(count2)

# 3. list comprehsnsion - basically its a shorter one line version loop of 1 solution but also creates a list contaning every vowel hence take extra space

count3 = len([char for char in s.lower() if char in "aeiou"])

print(count3)

# 4. sum() , for every match True is reurned and True is treated as 1 and sum fn counts it and gives vowel count
# this approach is best sum counts every true (treated as 1) and doesnt store any of that true(1) unlike the list comprehension verion
# so no extra space usage.
 
count4 = sum(char in "aeiou" for char in s.lower())

print(count4)

