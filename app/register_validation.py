import re

from app.utilities.utilities import *
from datetime import datetime


def validate_password(password) -> bool:

    # at least one capital letter
    capitalLetter = r"[A-Z]"
    # at least one small letter
    smallLetter = r"[a-z]"
    # at least one number
    oneNumber = r"\d"
    # min 8 characters, max 20
    numberOfCharacters = r".{8,20}"


    # boolean operation check it/cast bool
    return bool(re.search(capitalLetter, password) and re.search(smallLetter, password) and re.search(oneNumber, password) and re.search(numberOfCharacters, password))
    
def validate_email(email):

    email_pattern = r"((.*)@(.*))"
           
    # print(re.match(email_pattern, email, re.VERBOSE).groups())

    match = re.match(email_pattern, email, re.VERBOSE)
    
    if not match:  
        return False

    email, local_part, domain = match.groups()

    #CHECKING LOCAL PART OF AN EMAIL

    #If unquoted, it may use any of these ASCII characters:

    #uppercase and lowercase Latin letters A to Z and a to z
    #digits 0 to 9
    #printable characters !#$%&'*+-/=?^_`{|}~
    #dot ., provided that it is not the first or last character and provided also that it does not appear consecutively (e.g., John..Doe@example.com is not allowed)
    
    #If quoted, it may contain Space, Horizontal Tab (HT), any ASCII graphic except Backslash and Quote and a quoted-pair consisting of a Backslash followed by HT, Space or any ASCII graphic; it may also be split between lines anywhere that HT or Space appears. In contrast to unquoted local-parts, the addresses ".John.Doe"@example.com, "John.Doe."@example.com and "John..Doe"@example.com are allowed.
    
    if not re.match(r"^\".+\"$", local_part):
        
        # re.search(r"(^\.|\.$)") ??
        if re.search(r"^\.", local_part) or re.search(r"\.$", local_part):
            return False
    
        if re.search(r"\.{2,}", local_part):
            return False

        if not re.match(r"^[A-Za-z0-9!#$%&'*+-/=?^_`{|}~\.]{1,256}$", local_part):
            return False

    else:
        if not re.match(r"^[A-Za-z0-9!#$%&'*+-/=?^_`{|}~\.\s\"@]{1,256}$", local_part):
            return False
    

    #CHECKING DOMAIN PART OF AN EMAIL

    #uppercase and lowercase Latin letters A to Z and a to z;
    #digits 0 to 9, provided that top-level domain names are not all-numeric;
    #hyphen -, provided that it is not the first or last character.

    not_allowed_domains = ["web"]


    if not re.match(r"([A-Za-z0-9-\.]{1,63})", domain):
        return False

    if re.search(r"^\-", domain) or re.search(r"\-$", domain):
        return False

    if not re.search(r"\.", domain):
        return False

    if re.search(r"\.{2,}", domain):
            return False

    if re.search(r"\s", domain):
        return False

    if re.search(r"\.$", domain):
        return False

    for not_allowed_domain in not_allowed_domains:

        if re.search(fr".{not_allowed_domain}$", domain):
            return False

    return True


# TODO needs to be refactored
def validate_date_format(date):
    
    pattern = r"^(\d\d\d\d)-(\d\d)-(\d\d)$"

    groups = re.match(pattern, date)

    if not groups:
        return False
    
    year = int(groups.group(1))
    month = int(groups.group(2))
    day = int(groups.group(3)) 
    
    #TODO Should days in months to be checked? for example April 31 it's not correct.
    #TODO to validate days in months
    current_date = datetime.today()

    if year > current_date.year or year < 1900:
        return False

    if year == current_date.year:
        
        if month > current_date.month:
            return False

        if month == current_date.month and day > current_date.day:
            return False

    if month == 2:

        leap = is_leap_year(year)

        if leap and day > 29:
           return False

        if not leap and day > 28:
            return False     
    
    if month < 1 or month > 12:
        return False

    return True
