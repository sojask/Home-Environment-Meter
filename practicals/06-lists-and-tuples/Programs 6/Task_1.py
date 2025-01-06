def to_binary(n):
    if n <= 0:
        print("Input must be a positive integer.")
    return bin(n)[2:]

num = int(input("Enter a number: "))
print(f"The binary for {num} is: {to_binary(num)}")
