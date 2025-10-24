import re
from datetime import datetime


class UserValidation:
    """Handles validation for user-related inputs."""

    @staticmethod
    def validate_email(email: str) -> bool:
        """Check if the given email has a valid structure."""
        if email is None or not isinstance(email, str) or not email.strip():
            return False

        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.fullmatch(email_pattern, email))

    @staticmethod
    def validate_username(username: str) -> bool:
        """Ensure username is between 3–20 chars and contains only valid characters."""
        if username is None or not isinstance(username, str) or not username.strip():
            return False

        username_pattern = r"^[A-Za-z0-9_]{3,20}$"
        return bool(re.fullmatch(username_pattern, username))

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """Check if an Egyptian phone number is valid."""
        if phone is None or not isinstance(phone, str) or not phone.strip():
            return False

        phone_pattern = r"^(?:20)?(10|11|12|15)\d{8}$"
        return bool(re.fullmatch(phone_pattern, phone))

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        """Verify that the Egyptian national ID follows the correct format."""
        if national_id is None or not isinstance(national_id, str) or not national_id.strip():
            return False

        if not re.fullmatch(r"\d{14}", national_id):
            return False

        # Extract parts
        century_code = national_id[0]
        year = int(national_id[1:3])
        month = int(national_id[3:5])
        day = int(national_id[5:7])
        gov_code = int(national_id[7:9])

        # Validate century
        if century_code not in {"2", "3"}:
            return False

        # Validate date
        try:
            year_full = (1900 if century_code == "2" else 2000) + year
            datetime(year_full, month, day)
        except ValueError:
            return False

        # Validate governorate code range
        if not (1 <= gov_code <= 88):
            return False

        return True
