s="Deepanshu"
# 1. .count() this is best as method count is build for counting and no manual iteration is required.
count1 = s.count("e")

print(count1)

# 2.loop

count2 = 0

for char in s:
    if char == "e":
        count2 += 1

print(count2)

# 3.sum()
count3 = sum(char == "e" for char in s)

print(count3)

# 4. Counter  very usefull when want count of every caharcter in string
# stores char as key and count as value

from collections import Counter


counter = Counter(s)

print(counter["e"])