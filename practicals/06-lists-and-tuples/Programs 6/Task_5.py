import random
import string

def encrypt(message):
    interval = random.randint(2, 20)
    encrypted_message = ""

    for i, char in enumerate(message):
        encrypted_message += char

        if i < len(message) - 1:
            for _ in range(interval - 1):
                encrypted_message += random.choice(string.ascii_lowercase)

    return encrypted_message, interval


message = "send cheese"
encrypted_message, interval = encrypt(message)

print(f"Original Message: {message}")
print(f"Interval: {interval}")
print(f"Encrypted Message: {encrypted_message}")
