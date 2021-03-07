from app import register_validation as validation
from app.utilities.utilities import is_leap_year

import unittest


# TODO try pytest later
class RegexTesting(unittest.TestCase):

    def test_password_validation(self):

        passwords = {
            'abcAbc12': True,
            '123456A@': True,
            '123123abcABC': True,
            'Abc456': False,
            'abcabcabc': False,
            'AbcdefgAbcdefg': False}

        msg = "Test {0} expected {1} actual {2}"

        for password, expected in passwords.items():
            try:
                actual = validation.validate_password(password)
                self.assertEqual(actual, expected, msg.format(password, expected, actual))
            except AssertionError as error:
                print(error)

    # Not needed, external library email validation is used
    def test_email_validation(self):

        valid_emails = [
            "email@example.com",
            "firstname.lastname@example.com",
            "email@subdomain.example.com",
            "firstname+lastname@example.com",
            "\"email\"@example.com",
            "1234567890@example.com",
            "email@example-one.com",
            "_______@example.com",
            "email@example.name",
            "email@example.museum",
            "email@example.co.jp",
            "firstname-lastname@example.com"
        ]

        invalid_emails = [
            "plainaddress",
            "#@%^%#$@#$@#.com",
            "@example.com",
            "Joe Smith <email@example.com>",
            "email.example.com",
            "email@example@example.com",
            ".email@example.com",
            "email.@example.com",
            "email..email@example.com",
            "あいうえお@example.com",
            "email@example.com (Joe Smith)",
            "email@example",
            "email@-example.com",
            "email@example.web",
            "email@example..com"
        ]

        msg = "Test {0} expected {1} actual {2}"

        expected = True

        for email in valid_emails:
            try:
                actual = validation.validate_email(email)
                self.assertEqual(actual, expected, msg.format(email, expected, actual))
            except AssertionError as error:
                print(error)

        expected = False

        for email in invalid_emails:
            try:
                actual = validation.validate_email(email)
                self.assertEqual(actual, expected, msg.format(email, expected, actual))
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
            "05-03-1991": False,
            "1899-01-01": False}

        msg = "Test {0} expected {1} actual {2}"

        for date, expected in dates.items():

            try:
                actual = validation.validate_date_format(date)
                self.assertEqual(actual, expected, msg.format(date, expected, actual))
            except AssertionError as error:
                print(error)

    def test_is_leap_year(self):

        years = {
            2000: True,
            2004: True,
            2005: False,
            1997: False,
            1900: False
        }

        msg = "Test {0} expected {1} actual {2}"

        for year, expected in years.items():
            try:
                actual = is_leap_year(year)
                self.assertEqual(actual, expected, msg.format(year, expected, actual))
            except AssertionError as error:
                print(error)


if __name__ == "__main__":
    unittest.main()
