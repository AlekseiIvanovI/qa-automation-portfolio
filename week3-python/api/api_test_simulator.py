import requests
import json
from faker import Faker
from pathlib import Path
from datetime import datetime

fake = Faker()

BASE_URL = "https://jsonplaceholder.typicode.com"  # Free public API for practice

# 1. Generate fake user data


def generate_fake_user():
    return {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "website": fake.domain_name(),
        "company": fake.company(),
        "address": {
            "street": fake.street_address(),
            "city": fake.city(),
            "zipcode": fake.zipcode()
        }
    }

# 2. Test POST — create new user


def test_create_user():
    user = generate_fake_user()
    response = requests.post(f"{BASE_URL}/users", json=user)
    print(f"POST /users — Status: {response.status_code}")
    if response.status_code == 201:
        print("User created successfully")
        print(json.dumps(response.json(), indent=2)[:300] + "...")
    else:
        print("Failed to create user")
    return response.status_code == 201

# 3. Test GET — fetch users


def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    print(f"GET /users — Status: {response.status_code}")
    if response.status_code == 200:
        users = response.json()
        print(f"Fetched {len(users)} users")
        print(f"Sample: {users[0]['name']} ({users[0]['email']})")
    return response.status_code == 200

# 4. Test GET single user


def test_get_user(user_id=1):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print(f"GET /users/{user_id} — Status: {response.status_code}")
    if response.status_code == 200:
        user = response.json()
        print(
            f"User found: {user['name']} | Company: {user['company']['name']}")
    return response.status_code == 200

# 5. Test invalid endpoint (negative test)


def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid-endpoint")
    print(f"GET /invalid-endpoint — Status: {response.status_code}")
    return response.status_code == 404

# 6. Save report


def save_report(results):
    report = {
        "date": datetime.now().isoformat(),
        "tests_run": len(results),
        "passed": sum(results),
        "failed": len(results) - sum(results),
        "pass_rate": round(sum(results) / len(results) * 100, 2)
    }

    Path("api_reports").mkdir(exist_ok=True)
    filename = f"api_reports/report_{datetime.now():%Y%m%d_%H%M}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved: {filename}")
    print(f"Pass rate: {report['pass_rate']}%")


# RUN ALL TESTS
if __name__ == "__main__":
    print("WEEK 3 PRACTICE – API TESTING SIMULATOR")
    print("=" * 60)

    test_results = [
        test_get_users(),
        test_get_user(1),
        test_get_user(999),  # should fail
        test_create_user(),
        test_invalid_endpoint()
    ]

    save_report(test_results)
    print("=" * 60)
