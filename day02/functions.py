import numbers
import string


def return_integer() -> int:
    return print("print this")


print("--------------------------")


def name(str) -> string:
    return str[::-1]


print(name("Aylin"))

print("--------------------------")


def cube(num) -> int:
    return num * num * num


print(cube(10))
print("--------------------------")


def addition(num1, num2) -> numbers:  # numbers is parent class for float and int
    return num1 + num2


print(addition(100, 10.9))

print("--------------------------")


def addition1(num1: numbers, num2: numbers) -> numbers:  # this is parent class for float and int
    return num1 + num2


print(addition1(100, 100.9))

print("-------------------Pyhton does not have overloading -------")


def addition2(num1: numbers, num2: numbers, num3: numbers = 0) -> numbers:
    return num1 + num2 + num3


print(addition2(100, 100.9))
print(addition2(100, 100.9, 5))
