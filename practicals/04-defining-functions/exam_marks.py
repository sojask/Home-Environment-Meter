marks = []

for n in range(5):
    while len(marks) < 5:
        mark = int(input("Enter your mark: "))
        if mark >= 0 and mark <= 100:
            marks.append(mark)
        else:
            print("Invalid mark")
            
print("Highest mark is: ", max(marks))
print("Lowest mark is: ", min(marks))
print("Average mark is: ", sum(marks)/len(marks))



