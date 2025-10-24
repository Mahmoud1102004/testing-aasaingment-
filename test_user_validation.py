import unittest
from user_validation import UserValidation as UV


class TestUserValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(UV.validate_email("user@example.com"))

    def test_email_without_at(self):
        self.assertFalse(UV.validate_email("userexample.com"))

    def test_email_no_domain(self):
        self.assertFalse(UV.validate_email("user@"))

    def test_email_bad_tld(self):
        self.assertFalse(UV.validate_email("user@mail.c"))

    def test_email_with_subdomain(self):
        self.assertTrue(UV.validate_email("person@mail.company.com"))

    def test_email_with_symbols(self):
        self.assertTrue(UV.validate_email("ahmed.ali_99@mail.co"))

    def test_email_uppercase_letters(self):
        self.assertTrue(UV.validate_email("USER@MAIL.COM"))

    def test_email_contains_space(self):
        self.assertFalse(UV.validate_email("user name@mail.com"))

    def test_email_is_empty(self):
        self.assertFalse(UV.validate_email(""))

    def test_email_is_none(self):
        self.assertFalse(UV.validate_email(None))

    def test_valid_username(self):
        self.assertTrue(UV.validate_username("ahmed_samir"))

    def test_username_too_small(self):
        self.assertFalse(UV.validate_username("aa"))

    def test_username_too_big(self):
        self.assertFalse(UV.validate_username("ahmedsamirisaverylongusername"))

    def test_username_has_spaces(self):
        self.assertFalse(UV.validate_username("ahmed samir"))

    def test_username_has_special_chars(self):
        self.assertFalse(UV.validate_username("ahmed@123"))

    def test_username_with_numbers(self):
        self.assertTrue(UV.validate_username("ahmed123"))

    def test_username_is_empty(self):
        self.assertFalse(UV.validate_username(""))

    def test_username_is_none(self):
        self.assertFalse(UV.validate_username(None))

    def test_phone_vodafone(self):
        self.assertTrue(UV.validate_phone_number("01098765432"))

    def test_phone_orange(self):
        self.assertTrue(UV.validate_phone_number("01234567890"))

    def test_phone_etisalat(self):
        self.assertTrue(UV.validate_phone_number("01123456789"))

    def test_phone_we(self):
        self.assertTrue(UV.validate_phone_number("01599999999"))

    def test_phone_vodafone_with_country_code(self):
        self.assertTrue(UV.validate_phone_number("201098765432"))

    def test_phone_orange_with_country_code(self):
        self.assertTrue(UV.validate_phone_number("201234567890"))

    def test_phone_invalid_prefix(self):
        self.assertFalse(UV.validate_phone_number("01811111111"))

    def test_phone_too_short(self):
        self.assertFalse(UV.validate_phone_number("0101234567"))

    def test_phone_too_long(self):
        self.assertFalse(UV.validate_phone_number("010123456789"))

    def test_phone_contains_letters(self):
        self.assertFalse(UV.validate_phone_number("01012abc678"))

    def test_phone_is_empty(self):
        self.assertFalse(UV.validate_phone_number(""))

    def test_phone_is_none(self):
        self.assertFalse(UV.validate_phone_number(None))

    def test_valid_national_id(self):
        self.assertTrue(UV.validate_national_id("29812251234567"))

    def test_national_id_short(self):
        self.assertFalse(UV.validate_national_id("2981225123456"))

    def test_national_id_long(self):
        self.assertFalse(UV.validate_national_id("298122512345678"))

    def test_national_id_with_letters(self):
        self.assertFalse(UV.validate_national_id("29812AB1234567"))

    def test_national_id_wrong_century(self):
        self.assertFalse(UV.validate_national_id("19812251234567"))

    def test_national_id_wrong_month(self):
        self.assertFalse(UV.validate_national_id("29813251234567"))

    def test_national_id_wrong_day(self):
        self.assertFalse(UV.validate_national_id("29812323234567"))

    def test_national_id_invalid_gov_code(self):
        self.assertFalse(UV.validate_national_id("29812380034567"))

    def test_national_id_is_empty(self):
        self.assertFalse(UV.validate_national_id(""))

    def test_national_id_is_none(self):
        self.assertFalse(UV.validate_national_id(None))


if __name__ == "__main__":
    unittest.main()
