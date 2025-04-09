n='Automation Testing'

print(n[0]) #first
print(n[-1])#last #last index reverse
print(len(n))# total number of characters

n=n.lower() #STRING IS IMMUTABLE IN PYTHON therefore we assigned it to by itself
print(n)


print("-----------slicing practice")
s="Pyhton Programming Language"
print(s[7:])
print(s[0:18])
print(s[:18])

print("-----------reverse practice")

reversed_str=s[::-1]
print(reversed_str)

s2="Aylin"
reversed_s2=''.join(reversed(s2))
print(reversed_s2)

print("-----------compare 2 strings practice")
expected_title="Cydeo"
actual_title="CYDEO"

print(expected_title.lower()==actual_title.lower())