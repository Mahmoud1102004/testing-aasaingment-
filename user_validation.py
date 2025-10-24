import re
from datetime import datetime


class ValidationUtils:
    @staticmethod
    def check_email(value: str) -> bool:
        if not value or not isinstance(value, str) or not value.strip():
            return False
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.fullmatch(pattern, value))

    @staticmethod
    def check_username(name: str) -> bool:
        if not name or not isinstance(name, str) or not name.strip():
            return False
        pattern = r"^[A-Za-z0-9_]{3,20}$"
        return bool(re.fullmatch(pattern, name))

    @staticmethod
    def check_phone(num: str) -> bool:
        if not num or not isinstance(num, str) or not num.strip():
            return False
        pattern = r"^(?:20)?(10|11|12|15)\d{8}$"
        return bool(re.fullmatch(pattern, num))

    @staticmethod
    def check_national_id(nid: str) -> bool:
        if not nid or not isinstance(nid, str) or not nid.strip():
            return False
        if not re.fullmatch(r"\d{14}", nid):
            return False
        century = nid[0]
        yy = int(nid[1:3])
        mm = int(nid[3:5])
        dd = int(nid[5:7])
        gov = int(nid[7:9])
        if century not in {"2", "3"}:
            return False
        try:
            year = (1900 if century == "2" else 2000) + yy
            datetime(year, mm, dd)
        except ValueError:
            return False
        if not (1 <= gov <= 88):
            return False
        return True
