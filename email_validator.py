"""Script for validating email addresses"""
import re
import pandas as pd

students = pd.read_excel("./data/Ckodon Bio Submission Form (Responses).xlsx")
students = students.tail(len(students) - 769)

def validate(email: str)-> bool:
    is_valid = False
    regex = "^[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+$"
    email = email.strip()  # remove leading and trailing whitespace
    if re.search(regex, email):
        is_valid = True
    return is_valid

for email in students['Email']:
    print(validate(email), email)