
from collections import Counter
import re

log_file = "security.log"
failed_users = Counter()
failed_total = 0

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        if "Login failed" in line:
            match = re.search(r"user=(\w+)", line)
            if match:
                failed_users[match.group(1)] += 1
                failed_total += 1

print("=== Security Log Investigation ===")
print("Total failed logins:", failed_total)

print("\nFailed login attempts by user:")
for user, count in failed_users.items():
    print(f"{user}: {count}")

print("\nInvestigation findings:")
for user, count in failed_users.items():
    if count >= 3:
        print(f"ALERT: {user} has {count} failed attempts.")
