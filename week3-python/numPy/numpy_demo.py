import numpy as np
from datetime import datetime
import json
from pathlib import Path

np.random.seed(42)
test_count = 100
execution_times = np.random.exponential(scale=8, size=test_count)
execution_times = np.clip(execution_times, 0.5, 120)

statuses = np.random.choice(["PASS", "FAIL"], size=test_count, p=[0.85, 0.15])

total_time = float(execution_times.sum())
avg_time = float(execution_times.mean())
pass_count = int(np.sum(statuses == "PASS"))
slowest_5 = execution_times[np.argsort(execution_times)[-5:][::-1]].tolist()

report = {
    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "total_tests": test_count,
    "pass_rate": round(pass_count / test_count * 100, 2),
    "total_seconds": round(total_time, 2),
    "avg_seconds": round(avg_time, 2),
    "failed": test_count - pass_count,
    "slowest_5_sec": [round(float(x), 2) for x in slowest_5]
}

Path("reports").mkdir(exist_ok=True)
with open("reports/numpy_report.json", "w") as f:
    json.dump(report, f, indent=2)

# Final output
print("=" * 60)
print(f"Generated {test_count} test results")
print(f"Pass rate: {report['pass_rate']}%")
print(f"Total runtime: {report['total_duration_seconds']:.1f}s")
print(f"Average test: {report['average_duration']:.2f}s")
print(f"Failed: {report['failed_tests']}")
print("Report saved → final_reports/numpy_analysis.json")
print("=" * 60)
