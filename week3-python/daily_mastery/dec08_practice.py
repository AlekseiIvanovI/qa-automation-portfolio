"""
Daily Python Mastery – December 08, 2025
"""

from pathlib import Path
from datetime import datetime
import json
import random
from collections import Counter
import string

# 1. Strong password generator


def strong_password(length: int = 18) -> str:
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        pw = ''.join(random.choice(chars) for _ in range(length))
        if (any(c.islower() for c in pw) and
            any(c.isupper() for c in pw) and
            any(c.isdigit() for c in pw) and
                any(c in "!@#$%^&*" for c in pw)):
            return pw


# 2. Generate 20 fake users
users = [
    {
        "id": i + 1,
        "username": f"user{random.randint(1000, 9999)}",
        "email": f"user{i+1}@qa.test",
        "password": strong_password(),
        "created_at": datetime.now().isoformat()
    }
    for i in range(20)
]

# 3. Save to timestamped JSON
reports = Path("reports")
reports.mkdir(exist_ok=True)
filename = reports / f"users_{datetime.now():%Y%m%d_%H%M%S}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(users, f, indent=2, ensure_ascii=False)

# 4. Final report
print("DAILY MASTERY COMPLETE – DECEMBER 08, 2025")
print("=" * 60)
print(f"Generated {len(users)} users with strong passwords")
print(f"Report saved → {filename.resolve()}")
print(f"Time: {datetime.now():%H:%M:%S}")
print("=" * 60)
