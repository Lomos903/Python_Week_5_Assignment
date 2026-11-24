
import random
import string

def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# Generate an 8-character password
p1 = make_password()

# Generate a 12-character password
p2 = make_password(12)

# Print passwords and their lengths
print("Password:", p1)
print("Length:", len(p1))

print("Password:", p2)
print("Length:", len(p2))
