s1 = "Indore"
s2 = "Indoor"

# 1. set intersection , this is best as we only need common charcter and order doesnt matter

common=set(s1) & set(s2)

print(common)

# 2. loop , this good when we also want order preserved

common2 = []

for char in s1:
    if char in s2 and char not in common2:
        common2.append(char)

print(common2)