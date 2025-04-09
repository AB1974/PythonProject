"""
In Java :

for (int i=0 ; i<5  i++){

}
"""

for i in (range(0,5)):
    print(i)
print("==================")

s="Selenium"
for each in s:
    print(each)

print("==================")
reversed=""
for i in s [::-1]:
    reversed+=i
print(reversed)

print("==================")
for i in range(0,2):
    for x in range(0,2):
        print("selenium")
print("==================")

while True:
    print("Python Programming")
    break


print("==================")
score=int(input("Enter your score:\n")) # convert string to integer This is integer constructor


while score>100 or score < 0:
    score = int(input("Please re-enter:\n"))

if score>=0 :
    print("passed ")
else:
    print("failed")
