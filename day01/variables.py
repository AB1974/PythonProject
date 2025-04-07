"""
Java or static typed programming lang :
String str= "Wooden spoon";
int number= 100;

Python or dynamically typed programming lang;
data will be set during runtime
varName = data

"""
from ctypes import pythonapi

name_of_student ="Aylin"
print(type(name_of_student))
print(name_of_student)
name_of_student =10.5
print(type(name_of_student))
print(name_of_student)
name_of_student= True
print(type(name_of_student))
print(name_of_student)

# convert one type to another
age= '35'
num= int(age)
print(type(num))


# concatenation
prog_language="python"
version=3.13

print(f"I am learning {prog_language} with {version} version")
