import re

from datetime import date, timedelta

from email_validator import validate_email as check_email, EmailNotValidError


def validate_password(password) -> bool:
    # at least one capital letter
    capital_letter = r"[A-Z]"
    # at least one small letter
    small_letter = r"[a-z]"
    # at least one number
    one_number = r"\d"
    # min 8 characters, max 20
    number_of_characters = r".{8,20}"

    # boolean operation check it/cast bool
    return bool(re.search(capital_letter, password) and re.search(small_letter, password)
                and re.search(one_number, password) and re.search(number_of_characters, password))


def validate_email(email: str) -> bool:

    try:
        is_valid = check_email(email)

    except EmailNotValidError as e:
        print(str(e))
        return False

    return True


# TODO needs to be refactored
def validate_date_format(input_date: str) -> bool:

    pattern = r"^(\d\d\d\d)-(\d\d)-(\d\d)$"

    match = re.match(pattern, input_date)

    if not match:
        return False

    year, month, day = list(map(lambda x: int(x), match.groups()))

    try:
        user_date = date(year, month, day)
    except ValueError as e:
        return False

    current_date = date.today()

    if (current_date - user_date) < timedelta():
        return False

    return True
