items=["pen","laptop","book","camera"]
print(type(items))
print(len(items))
items.append("purple")
print(items)
items.remove("book")
print(items)
items.pop(-2)
print(items)
items.extend( ("extend","aylin") )
print(items)

languages = ("Java","c#","python","js")
temp_list=list(languages)

temp_list.pop(1)
print(temp_list)
temp_list.remove("js")
print(temp_list)
languages=tuple(temp_list) #tuple
print(languages)

for i in languages:
    print(i)


print("==========")

nums=[]
for i in range(1,31):
    nums.append(i)
print(nums)

divisible_by_three= [p for p in nums if p % 3 ==0]
print(divisible_by_three)
