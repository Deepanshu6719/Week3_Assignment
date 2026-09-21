# Remove given character from string
s="Deepanshu"

# 1. replace(), this best approach as we want to remove a character
#  from the string the method itself is designed to do so and is short and simple
result1 = s.replace("a", "")

print(result1)

# 2. loop
result2=""

for char in s:
    if char != "a":
        result2+=char

print(result2)        

# 3. list comprehension

result3=''.join(char for char in s if char != "a")

print(result3)

# 4. filter()

result4=''.join(filter(lambda char:char != "a",s))

print(result4)