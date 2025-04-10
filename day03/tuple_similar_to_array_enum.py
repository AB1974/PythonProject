browsers=("Chrome","Safari","Firefox","IE","Edge")
print(type(browsers))
print(len(browsers))
print(browsers[-1])
print(browsers[0])
print(browsers[-2])

print(browsers[:5])
print(browsers[1:])

a1=browsers[1:-1]
print(a1)
print(a1[1:])

reversed_tuple=' '.join(browsers) # converts to string
print(reversed_tuple)

reversed_tuple2 =tuple(reversed(browsers))
print(reversed_tuple2)

reversed_tuple3=tuple(reversed(browsers[::-1]))
print(reversed_tuple3)

for each in browsers:
    print(each)
print(" multi-------tuple")
group_scores=((10,20,30),(40,50,60))

for i in group_scores:
    print(i)
    for j in i:
        print(j)
print(" merge -------tuple")

t1=(1,3)
t2=(4,5,6)
t3=(7,10,60)
merged_tuple=t1+t2+t3
print(merged_tuple)
