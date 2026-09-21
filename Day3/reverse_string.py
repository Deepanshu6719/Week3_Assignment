s="Deepanshu"

# 1. Slicing (the shortest and price verion with no unnecassry code and can say that is best approach )

reverse1=s[::-1]
print(reverse1)

# 2. using reversed() method this method return a iterator object hence to get string .join() is must 

reverse2 = ''.join(reversed(s))

print(reverse2)

# 3.loop this is useful for learning purpose to understand how solution works

reverse3 = ""

for char in s:
    reverse3 = char + reverse3

print(reverse3)

# 4. using indexes in range()

reverse4 = ""

for i in range(len(s) - 1, -1, -1):
    reverse4 += s[i]

print(reverse4)