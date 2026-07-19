# Password Generator
# CodeSoft Internship - Task 3

import random
import string

print("===== PASSWORD GENERATOR =====")

# Ask the user for password length
length = int(input("Enter the password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("\nGenerated Password:")
print(password)
