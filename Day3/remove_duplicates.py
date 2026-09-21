numbers = [1, 2, 2, 3, 4, 4, 5, 7, 8, 7]
# 1. Set , make list into set directly remove duplicate so short and easy way
# but one issue set doesnt guarentee original list ordering 
result1 = list(set(numbers))

# 2.loop + set,  loops through list and append in set and in new list if elemnet not already present


result2 = []
seen = set()

for num in numbers:
    if num not in seen:
        result2.append(num)
        seen.add(num)

print(result2)

# 3. dictionary  , preserve the insertion order , stores the items in list in keys and then convert the keys in dict to list to get unique list
#  this is best solution as it preserve the order of list and have very cincise solution
result3 = list(dict.fromkeys(numbers))

print(result3)

