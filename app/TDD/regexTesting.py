import unittest
import re

# TODO with file in this folder app/TDD/regexTesting.py can't find app.utilities need to be fixed.
from app.utilities import register_validation as validation

# TODO try pytest later
class regexTesting(unittest.TestCase):
    
    def test_password_validation(self):

        passwords = {
            'Roszek91' : True,
            'Tomeczek1991': True,
            'LubiePlacki12@@@:': True,
            'Tom91': False,
            'tomekbomek': False,
            'TomeczekSromeczek': False}

        msg = "Test {0} expected {1} actual {2}"

        for password, result in passwords.items():
            try:
                self.assertEqual(validation.validate_password(password), result, msg.format(password, result, validation.validate_password(password)))
            except AssertionError as error:
                print(error)

        
    def test_email_validation(self):

        emails = {
            "tomaszgroch@gmail.com": True,
            "tomkielolsd91@gmail.com": True,
            "tomibomi@o2.pl" : True,
            "lubieplacki": False,
            "9232193923": False,
            "czoko@o2.plO2@02.com": False}

        msg = "Test {0} expected {1} actual {2}"

        for email, result in emails.items():
            try:
                self.assertEqual(validation.validate_email(email), result, msg.format(email, result, validation.validate_email(email)))
            except AssertionError as error:
                print(error)
  

    def test_date_validation(self):

        dates = {
            "1991-05-05": True,
            "1992-10-12": True,
            "2005-05-29": True,
            "1975-11-02": True,
            "2000-02-29": True,
            "2004-02-29": True,
            "2008-02-29": True,
            "2004-02-28": True,
            "2003-02-28": True,
            "2003-02-29": False,
            "2005-02-29": False,
            "2012-13-05": False,
            "1992-5-9": False,
            "1991": False,
            "1991-05": False,
            "1991/05/05": False,
            "2012-13-05": False, 
            "05-03-1991": False} 

        msg = "Test {0} expected {1} actual {2}"

        for date, result in dates.items():

            try:            
                self.assertEqual(validation.validate_date_format(date), result, msg.format(date, result, validation.validate_date_format(date)))
            except AssertionError as error:
                    print(error)


    def test_is_leap_year(self):

        years = {
                2000: True,
                2004: True,
                2005: False,
                1997: False,
                1900: False}
        
        msg = "Test {0} expected {1} actual {2}"

        for year, result in years.items():
            try:
                self.assertEqual(validation.is_leap_year(year), result, msg.format(year, result, validation.is_leap_year(year)))
            except AssertionError as error:
                print(error)


if __name__ == "__main__":
    unittest.main()
