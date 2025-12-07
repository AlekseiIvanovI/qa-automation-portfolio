import json
import csv
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter, namedtuple
import subprocess
import random
import string
from faker import Faker

fake = Faker()

# 1. Generate 50 fake test results
TestResult = namedtuple("TestResult", ["name", "status", "duration", "tags"])


def generate_fake_results(count=50):
    names = [f"test_{fake.word()}_{i}" for i in range(1, count+1)]
    statuses = ["PASS"] * 42 + ["FAIL"] * 8
    tags_pool = ["smoke", "regression", "api", "ui", "critical"]

    results = []
    for _ in range(count):
        name = random.choice(names)
        status = random.choice(statuses)
        duration = round(random.uniform(0.5, 15.0), 2)
        tags = random.sample(tags_pool, k=random.randint(0, 3))
        results.append(TestResult(name, status, duration, tags))
    return results


results = generate_fake_results(50)

# 2. Save to JSON + CSV + SQLite
reports_dir = Path("final_reports")
reports_dir.mkdir(exist_ok=True)

# JSON
json_path = reports_dir / "test_results.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump([r._asdict() for r in results], f, indent=2)

# CSV
csv_path = reports_dir / "test_results.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=TestResult._fields)
    writer.writeheader()
    writer.writerows([r._asdict() for r in results])

# SQLite
db_path = reports_dir / "test_results.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    name TEXT, status TEXT, duration REAL, tags TEXT
)
""")
for r in results:
    cursor.execute("INSERT INTO results VALUES (?, ?, ?, ?)",
                   (r.name, r.status, r.duration, ",".join(r.tags)))
conn.commit()
conn.close()

# 3. Analysis with collections.Counter
status_count = Counter(r.status for r in results)
tag_count = Counter(tag for r in results for tag in r.tags)

# 4. Run git status via subprocess
try:
    git_status = subprocess.check_output(["git", "status", "--short"]).decode()
except:
    git_status = "Git not available"

# 5. Final report
print("=" * 70)
print(f"FINAL PYTHON MASTERY – {datetime.now():%Y-%m-%d %H:%M}")
print("=" * 70)
print(f"Generated {len(results)} test results")
print(f"Pass rate: {status_count['PASS']/len(results)*100:.1f}%")
print(f"Total duration: {sum(r.duration for r in results):.1f}s")
print(
    f"Most common tag: {tag_count.most_common(1)[0][0] if tag_count else 'N/A'}")
print(f"Reports saved to: {reports_dir.resolve()}")
print(f"Git status:\n{git_status or 'Clean'}")
print("=" * 70)
