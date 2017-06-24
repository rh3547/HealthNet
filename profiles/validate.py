"""
Validation for all field input
"""
import re

from django.contrib.auth.models import User


class InvalidInput(Exception):
    pass


# Ensure an username is unique and at least 5 alphanumeric characters
def validateUser(username):
    user = User.objects.filter(username=username)

    if user:
        raise InvalidInput("That username is already taken , please choose another.")
    elif len(username) < 4:
        raise InvalidInput("Username should contain at least 5 characters.")
    elif not re.search(r'^\w+$', username):
        raise InvalidInput("Username can only contain alphanumeric characters and the underscore.")
    return username


# Ensure an email is unique and matches correct email format
def validateEmail(email):
    for user in User.objects.iterator():
        if email is user.email:
            raise InvalidInput("That email is already registered.")

    if re.search(r'^[^@]+@[^@]+\.[^@]+$', email):
        return email
    else:
        raise InvalidInput("Email entered is not valid!")


# Ensure a password is at least 1 character.. (not empty)
def validatePass(password):
    if len(password) > 1:
        return password
    else:
        raise InvalidInput("You must enter a password.")
