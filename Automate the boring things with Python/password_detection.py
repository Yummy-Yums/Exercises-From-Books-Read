import re

pattern = r'[a-zA-Z\d]{8,}'
passwords = [
    "Password123",
    "SecurePass",
    "weak123",
    "NoDigitUpper",
    "short"
]

for password in passwords:
    if re.match(pattern, password):
        print(f"'{password}' is a strong password.")
    else:
        print(f"'{password}' is not a strong password.")
