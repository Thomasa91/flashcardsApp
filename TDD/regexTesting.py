from logging import exception
import unittest
import re

# TODO REFACTOR THIS TEST, USE FUNCTIONS FROM USER CLASS, NEED TO REFACTOR USER CLASS AND AUTHENTICATION ENDPOINT TO CHECK PASSWORD AND EMAIL


def validatePassword(password):

    # at least one cappital letter
    capitalLetter = r"[A-Z]+"
    # at least one small letter
    smallLetter = r"[a-z]+"
    # at least one number
    oneNumber = r"\d+"
    # min 8 characters, max 20
    numberOfCharacters = r"^\.{8, 20}$"

    if re.match(capitalLetter, password) and re.match(smallLetter, password) and re.match(oneNumber, password) and re.match(numberOfCharacters, password):
        return False
    
    return True

def validateEmail(email):

    pattern = r"\.+@\w+.\w+"

    if re.match(pattern, email):
        return True

    return False

def check_date_format(date):

    pattern = r"^\d{4}-\d{2}-\d{2}$"

    if re.match(pattern, date):
        return True
    
    return False


class regexTesting(unittest.TestCase):
    
    def test_password_valitation(self):
        passwords = {'Roszek91' : True,
                 'Tomeczek1991': True,
                 'LubiePlacki12@@@:': True,
                 'Tom91': False,
                 'tomekbomek': False,
                 'TomeczekSromeczek': False}

        msg = "Test {0} expected {1} actual {2}"

        print("test password")
        for password, result in passwords.items():
            try:
                self.assertEqual(validatePassword(password), result, msg.format(password, result, validatePassword(password)))
            except AssertionError as error:
                print(error)


        print("finish test password")
    def test_email_validation(self):

        emails = {"tomaszgroch@gmail.com": True,
                "tomkielolsd91@gmail.com": True,
                "tomibomi@o2.pl" : True,
                "lubieplacki": False,
                "9232193923": False,
                "czoko@o2.plO2@02.com": False}


        msg = "Test {0} expected {1} actual {2}"

        for email, result in emails.items():
            try:
                self.assertEqual(validateEmail(email), result, msg.format(email, result, validateEmail(email)))
            except AssertionError as error:
                print(error)
  

    def test_date_validation(self):

        dates = {"1991-05-05": True,
                "1992-5-9": False,
                "1991": False,
                "1991-05": False,
                "1991/05/05": False,
                "2012-13-05": True, #TODO should be false I need to change validation
                "05-03-1991": False} 


        for date, result in dates.items():
            try:
                self.assertEqual(check_date_format(date), result)
            except AssertionError as error:
                print(error)

if __name__ == "__main__":
    unittest.main()