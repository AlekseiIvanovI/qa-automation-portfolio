# qa_utils/validator.py
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

    def getErrors(self, password: str):
        errors = []
        if len(password) < 12:
            errors.append("Password must be at least 12 characters")
        if not any(c.isupper() for c in password):
            errors.append("At least one uppercase required")
        if not any(c.islower() for c in password):
            errors.append("At least one lowercase required")
        if not any(c.isdigit() for c in password):
            errors.append("At least one digit required")
        if not any(c in self.SPECIAL_CHARS for c in password):
            errors.append("At least one special char required")
        return errors
