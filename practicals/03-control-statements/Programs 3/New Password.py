bad_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password between 8 and 12 characters: ")

    if len(password1) < 8 or len(password1) > 12:
        print("Invalid: Password must be between 8 and 12 characters long. Please try again.")

    elif password1.lower() in [p.lower() for p in bad_passwords]:
        print("Error: This password is too common. Please try again.")
    else:
        password2 = input("Re-enter your password: ")

        if password1 == password2:
            print("Password Set")
            break
        else:
            print("Error: Passwords do not match. Please try again.")
