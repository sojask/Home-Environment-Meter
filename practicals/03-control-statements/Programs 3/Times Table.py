while True:
    number = int(input("Enter a number between -12 and 12: "))

    if -12 <= number <= 12:
        break
    else:
        print("Please enter a number between -12 and 12.")

if number < 0:
    for i in range(12, -1, -1):
        print(i, "x", number, "=", i * number)

else:
    for i in range(13):
        print(i, "x", number, "=", i * number)