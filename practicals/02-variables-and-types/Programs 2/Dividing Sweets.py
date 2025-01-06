total = int(input("How many sweets are in total?: "))
pupils = int(input("How many pupils are in today?: "))

sweets_each = total // pupils
leftovers = total % pupils

print("Each pupil gets", sweets_each, "sweets.")
print("There will be", leftovers, "sweets left over.")
