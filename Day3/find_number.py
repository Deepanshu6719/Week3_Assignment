list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 5]

# 1. using set difference
# simple and no manual looping

missing = set(list1) - set(list2)

print(missing)


# 2. loop , for manual searching of missing  number and logic understanding
for num in list1:
    if num not in list2:
        print(num)


#3. list comprehension , same as above but in one line
missing2 = [num for num in list1 if num not in list2]

print(missing2) 