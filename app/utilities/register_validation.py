import re

def validate_password(password):

    # at least one capital letter
    capitalLetter = r"[A-Z]"
    # at least one small letter
    smallLetter = r"[a-z]"
    # at least one number
    oneNumber = r"\d"
    # min 8 characters, max 20
    numberOfCharacters = r".{8,20}"

    if re.search(capitalLetter, password) and re.search(smallLetter, password) and re.search(oneNumber, password) and re.search(numberOfCharacters, password):
        return True
    
    return False


def validate_email(email):

    pattern = r"^(\w+@\w+\.\w+)$"

    if re.match(pattern, email):
        return True
    
    return False


# TODO needs to be refactored
def validate_date_format(date):


    # year_pattern = r"([1-2][0-9][0-9][0-9])"
    # month_pattern = r"(0[1-9])|(1[0-2])"
    # day_pattern = r"([0-2][0-9])|(3[0-1])"

    pattern = '' 
    
    year = re.search("[1-2][0-9][0-9][0-9]", date).group()

    year = int(year)

    if is_leap_year(year):
        pattern = "([1-2][0-9][0-9][0-9])-(((0[1,3-9]|1[0-2])-([0-2][0-9]|3[0-1]))|(02-[0-2][0-9]))"
    else:
        pattern = "([1-2][0-9][0-9][0-9])-(((0[1,3-9]|1[0-2])-([0-2][0-9]|3[0-1]))|(02-[0-2][0-8]))"

    if re.match(pattern, date):
        return True

    return False


def is_leap_year(year):

    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True

    return False
