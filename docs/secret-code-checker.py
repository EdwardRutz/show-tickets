# while loop demo

import sys

MASTER_SECRET_CODE = "opensesame"

secret_code = input("Enter secret code?")
attempt_count = 1
while secret_code != MASTER_SECRET_CODE:
    if attempt_count >3:
        sys.exit("Too many invalid password attempts.")
    secret_code = input("Invalid secret code, try again...")
    attempt_count += 1
print("Welcome to secret town!")
