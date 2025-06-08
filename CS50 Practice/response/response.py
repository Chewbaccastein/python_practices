from validator_collection import validators

user_email = input("What's your email address? ")
try:
    email_address = validators.email(user_email, allow_empty=True)
    if email_address:
        print("Valid")
    else:
        print("Invalid")
except (ValueError, TypeError):
    print("Invalid")
