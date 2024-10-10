count = 10
while count > 0:
    print("Countdown is ", count)
    count -= 1

for n in range(20, 0, -1):
    print(n, "doubled is", n * 2)

for n in range(2, 12, 2):
    print(n, "to the power of", n, "=", n ** n)

value = int(input("enter a number: "))
for n in range(2, value//2):
    if value % n == 0:
        print(value, "is not a prime number")
        break
    else:
        print(value, "is a prime number")

grades = [20, 50, 43, 33, 90, 15]
pass_mark = 40
passes = 0
total = 0
for grade in grades:
    if grade < pass_mark:
        continue
    passes += 1
    total += grade
print("average pass mark was", total/passes)
