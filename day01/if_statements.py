from importlib.metadata import pass_none

browser_name= "safari"

if browser_name =="chrome":
    print("Chrome browser is selected") # there is an indentation
elif browser_name=="firefox":
    print("Firefox browser is selected")
    print("Opening firefox browser")
else:
    print("Safari browser is selected")
    print("Opening safari browser")

print("===========-------------------")

score = -200

if 0 <= score <= 100:

    if score >= 60:
        print("Passed the exam")
    else:
        print("Failed the exam")

else:
    print("Failed the exam")

print("-----------------------------------------")

if True:
    pass
else:
    pass


def function_name():
    print("This is a function")
    pass


class Animal:
    pass


