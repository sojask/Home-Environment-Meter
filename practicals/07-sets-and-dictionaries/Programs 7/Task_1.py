def sorted_letters(string):
    letters = []

    for char in string:
        if char.isalpha() and char.lower() not in letters:
            letters.append(char.lower())

    letters.sort()
    return letters

string = input("Enter a string: ")
sorted_unique_letters = sorted_letters(string)

print(f"Original String: {string}")
print(f"The uniquely sorted list for this string is: {sorted_unique_letters}")
