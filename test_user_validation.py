import unittest
from user_validation import UserValidation


class UserValidationTests(unittest.TestCase):

    # ---------------- Email Tests ----------------
    def test_email_valid(self):
        self.assertTrue(UserValidation.validate_email("user@example.com"))

    def test_email_missing_at_symbol(self):
        self.assertFalse(UserValidation.validate_email("userexample.com"))

    def test_email_missing_domain(self):
        self.assertFalse(UserValidation.validate_email("user@"))

    def test_email_invalid_tld(self):
        self.assertFalse(UserValidation.validate_email("user@mail.c"))

    def test_email_with_subdomain(self):
        self.assertTrue(UserValidation.validate_email("user@mail.company.com"))

    def test_email_with_special_characters(self):
        self.assertTrue(UserValidation.validate_email("ramy.gomaa_21@mail.co"))

    def test_email_uppercase(self):
        self.assertTrue(UserValidation.validate_email("USER@MAIL.COM"))

    def test_email_with_space(self):
        self.assertFalse(UserValidation.validate_email("user name@mail.com"))

    def test_email_empty(self):
        self.assertFalse(UserValidation.validate_email(""))

    def test_email_none(self):
        self.assertFalse(UserValidation.validate_email(None))

    # ---------------- Username Tests ----------------
    def test_username_valid(self):
        self.assertTrue(UserValidation.validate_username("ramy_gomaa"))

    def test_username_too_short(self):
        self.assertFalse(UserValidation.validate_username("ab"))

    def test_username_too_long(self):
        self.assertFalse(UserValidation.validate_username("ramygomaaisaverylongusername"))

    def test_username_with_spaces(self):
        self.assertFalse(UserValidation.validate_username("ramy gomaa"))

    def test_username_with_symbols(self):
        self.assertFalse(UserValidation.validate_username("ramy@123"))

    def test_username_with_digits(self):
        self.assertTrue(UserValidation.validate_username("ramy123"))

    def test_username_empty(self):
        self.assertFalse(UserValidation.validate_username(""))

    def test_username_none(self):
        self.assertFalse(UserValidation.validate_username(None))

    # ---------------- Phone Tests ----------------
    def test_phone_valid_vodafone(self):
        self.assertTrue(UserValidation.validate_phone_number("01012345678"))

    def test_phone_valid_orange(self):
        self.assertTrue(UserValidation.validate_phone_number("01234567890"))

    def test_phone_valid_etisalat(self):
        self.assertTrue(UserValidation.validate_phone_number("01198765432"))

    def test_phone_valid_we(self):
        self.assertTrue(UserValidation.validate_phone_number("01555555555"))

    def test_phone_with_country_code_vodafone(self):
        self.assertTrue(UserValidation.validate_phone_number("201012345678"))

    def test_phone_with_country_code_orange(self):
        self.assertTrue(UserValidation.validate_phone_number("201234567890"))

    def test_phone_invalid_prefix(self):
        self.assertFalse(UserValidation.validate_phone_number("01812345678"))

    def test_phone_too_short(self):
        self.assertFalse(UserValidation.validate_phone_number("0101234567"))

    def test_phone_too_long(self):
        self.assertFalse(UserValidation.validate_phone_number("010123456789"))

    def test_phone_with_characters(self):
        self.assertFalse(UserValidation.validate_phone_number("01012abc678"))

    def test_phone_empty(self):
        self.assertFalse(UserValidation.validate_phone_number(""))

    def test_phone_none(self):
        self.assertFalse(UserValidation.validate_phone_number(None))

    # ---------------- National ID Tests ----------------
    def test_national_id_valid(self):
        self.assertTrue(UserValidation.validate_national_id("29812251234567"))

    def test_national_id_too_short(self):
        self.assertFalse(UserValidation.validate_national_id("2981225123456"))

    def test_national_id_too_long(self):
        self.assertFalse(UserValidation.validate_national_id("298122512345678"))

    def test_national_id_with_letters(self):
        self.assertFalse(UserValidation.validate_national_id("2981225AB34567"))

    def test_national_id_invalid_century(self):
        self.assertFalse(UserValidation.validate_national_id("19812251234567"))

    def test_national_id_invalid_month(self):
        self.assertFalse(UserValidation.validate_national_id("29813251234567"))

    def test_national_id_invalid_day(self):
        self.assertFalse(UserValidation.validate_national_id("29812323234567"))

    def test_national_id_invalid_governorate(self):
        self.assertFalse(UserValidation.validate_national_id("29812380034567"))

    def test_national_id_empty(self):
        self.assertFalse(UserValidation.validate_national_id(""))

    def test_national_id_none(self):
        self.assertFalse(UserValidation.validate_national_id(None))


if __name__ == "__main__":
    unittest.main()
