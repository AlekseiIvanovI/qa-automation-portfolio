class Account():
    def __init__(self, name, url, username, password, category):
        self.name = name
        self.url = url
        self.username = username
        self.password = password
        self.category = category


class PasswordManager:
    def __init__(self):
        self.acc_list = []
        self.validator = PasswordValidator()

    def get_valid_password(self):
        while True:
            password_input = input("Enter a password: ")
            if self.validator.validate(password_input):
                return password_input
            else:
                self.validator.getErrors(password_input)
                for error in self.validator.getErrors(password_input):
                    print(error)
                print("Try again")

    def add_account(self):
        username = input("Enter username: ")
        url = input("Enter url: ")
        name = input("Enter name: ")
        category = input("Enter a category: ")
        pwd = self.get_valid_password()
        self.acc_list.append(Account(name, url, username, pwd, category))
        print("Account added successfully!\n")


class PasswordValidator():
    def __init__(self):
        pass

    def validate(self, password: str):
        return (
            True if len(password) >= 12 and
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char.isupper() for char in password) and
            any(char in "!@#$%^&*" for char in password) else False
        )

    def getErrors(self, password: str) -> list[str]:
        errors = []
        if len(password) < 12:
            errors.append("Password must be at least 12 characters long")

        if not any(char.isdigit() for char in password):
            errors.append("At least one digit required")

        if not any(char.isupper() for char in password):
            errors.append("At least one uppercase character required")

        if not any(char.islower() for char in password):
            errors.append("At least one lowercase character required")

        if not any(char in "!@#$%^&*" for char in password):
            errors.append("At least one special character required")
        return errors


if __name__ == "__main__":
    print("Password Manager")
    print("=" * 55)

    manager = PasswordManager()

    while True:
        print("\nMenu:")
        print("1. Add new account")
        print("2. List all accounts")
        print("3. Exit")

        choice = input("\nSelect option (1-3): ").strip()

        if choice == "1":
            manager.add_account()

        elif choice == "2":
            if not manager.acc_list:
                print("No accounts saved yet.\n")
            else:
                print(f"\nSaved accounts ({len(manager.acc_list)}):")
                print("-" * 55)
                for i, acc in enumerate(manager.acc_list, 1):
                    print(f"{i}. {acc.name} ({acc.category})")
                    print(f"   URL      : {acc.url}")
                    print(f"   Username : {acc.username}")
                    print(f"   Password : {'*' * len(acc.password)}")
                    print()

        elif choice == "3":
            print("Goodbye! Your accounts are safe.")
            break

        else:
            print("Invalid choice. Try again.")
