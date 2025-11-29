# 1. TestUser – with properties and private attribute
class TestUser:
    def __init__(self, name, email, password, role="user"):
        self.name = name
        self.email = email
        self.__password = password
        self.role = role

    @property
    def isAdmin(self):
        return self.role == "admin"

    @property
    def full_info(self):
        return f"Name: {self.name}, Email: {self.email}, Role: {"admin" if self.isAdmin else "user"}"

    @property
    def password(self):
        return "********"

# 2. TestResult – with __str__ and property


class TestResult:
    def __init__(self, test_name, status, duration):
        self.test_name = test_name
        self.status = status.upper()
        self.duration = duration

    @property
    def is_passed(self):
        return self.status == "PASS"

    @property
    def __str__(self):
        return f"{'PASS' if self.is_passed else 'FAIL'} - {self.test_name} ({self.duration:.2f}s)"


class TestSuite:
    def __init__(self, name):
        self.name = name
        self.results: list[TestResult] = []

    def add_result(self, result: TestResult):
        self.results.append(result)

    @property
    def pass_rate(self):
        if not self.results:
            return 0.0
        passed = sum(1 for x in self.results if x.is_passed)
        return passed / len(self.results) * 100

    @property
    def total_duration(self):
        return sum(x.duration for x in self.results)

    @property
    def failed_tests(self) -> list[str]:
        return [x.test_name for x in self.results if not x.is_passed]


# Demo
if __name__ == "__main__":
    user1 = TestUser("Aleksei", "aleksei@test.com", "SuperSecret123!", "admin")
    user2 = TestUser("John", "john@test.com", "12345", "user")

    print(user1.full_info, user2.full_info, sep="\n")
    print(user1.password, user2.password, sep="\n")
    print(f"Is user an admin: {user1.isAdmin}",
          f"Is user an admin: {user2.isAdmin}", sep="\n")

    suite = TestSuite("Regression Suite")
    suite.add_result(TestResult("login_valid", "PASS", 2.4))
    suite.add_result(TestResult("checkout_flow", "FAIL", 8.1))
    suite.add_result(TestResult("search_test", "PASS", 1.9))

    print(f"\n{suite.name}")
    print(f"Pass rate: {suite.pass_rate:.1f}%")
    print(f"Total time: {suite.total_duration:.2f}s")
    print(f"Failed: {suite.failed_tests}")
