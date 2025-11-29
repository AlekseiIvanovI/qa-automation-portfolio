class TestUser():
    def __init__(self, password, user, email, role="user"):
        self.__password = password
        self.user = user
        self.email = email
        self.role = role

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def password(self):
        return "Password: **********"

    @property
    def full_info(self):
        return f"Name: {self.user} Email: {self.email} Role: {"admin" if self.is_admin else "user"}"


class TestResult():
    def __init__(self, test_name, status, duration):
        self.test_name = test_name
        self.status = status.upper()
        self.duration = duration

    @property
    def is_passed(self):
        return self.status == "PASS"

    def __str__(self):
        return f"{'PASS' if self.is_passed else 'FAIL'} - {self.test_name} ({self.duration:.2f}s)"


class TestSuite():
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
        if not self.results:
            return 0.0
        failed = sum(1 for x in self.results if not x.is_passed)
        return failed / len(self.results) * 100


if __name__ == "__main__":
    user1 = TestUser("21312sqw", "Aleksei", "aleks@gmail.com", "admin")
    user2 = TestUser("fsaeqwf24231", "John", "john@gmail.com", "user")
    print(user1.full_info, user2.full_info, sep="\n")
    print(f"{user1.user} {user1.password}",
          f"{user2.user} {user2.password}", sep="\n")

    print(f"Is user {user1.user} an admin: {user1.is_admin}",
          f"Is user {user2.user} an admin: {user2.is_admin}", sep="\n")

    suite = TestSuite("Regression Suite")
    suite.add_result(TestResult("login valid", "PASS", 2.3))
    suite.add_result(TestResult("checkout_flow", "FAIL", 8.3))
    suite.add_result(TestResult("search test", "PASS", 1.2))

    print(f"\n{suite.name}")
    print(f"Passed: {suite.pass_rate:.1f}%")
    print(f"Failed: {suite.failed_tests:.1f}%")
    print(f"Total time: {suite.total_duration:.1f}s")
