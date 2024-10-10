age = int(input("Enter your age: "))
if age >= 18 and age <= 29:
    print("You are still kinda young i guess")
elif age > 100:
    print("you are very old,")
    print("well done!")
elif age > 80:
    print("you are fairly old")
    print("pretty good!")
elif age > 40:
    print("you are middle aged")
    print("never mind")
elif age >= 30 and age <= 40:
    print("You are in the prime of life")
else:
    print("you are not very old - yet")