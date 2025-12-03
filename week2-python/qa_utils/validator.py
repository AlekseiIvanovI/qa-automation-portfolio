# qa_utils/validator.py
from typing import List


class PasswordValidator:
    SPECIAL_CHARS = "!@#$%^&*"

    def validate(self, password: str) -> bool:
        return all([
            len(password) >= 12,
            any(c.isupper() for c in password),
            any(c.islower() for c in password),
            any(c.isdigit() for c in password),
            any(c in self.SPECIAL_CHARS for c in password),
        ])

    def getErrors(self, password: str) -> List[str]:
        errors = []
        if len(password) < 12:
            errors.append("Password must be at least 12 characters long")
        if not any(c.isupper() for c in password):
            errors.append("At least one uppercase character required")
        if not any(c.islower() for c in password):
            errors.append("At least one lowercase character required")
        if not any(c.isdigit() for c in password):
            errors.append("At least one digit required")
        if not any(c in self.SPECIAL_CHARS for c in password):
            errors.append("At least one special character required")
        return errors
