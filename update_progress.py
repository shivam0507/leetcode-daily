import requests
import json
from datetime import datetime

# Replace with your LeetCode username
LEETCODE_USERNAME = "guptashivam0507"

# LeetCode GraphQL API to fetch solved problems
LEETCODE_API_URL = "https://leetcode.com/graphql"

QUERY = """
{
  matchedUser(username: "%s") {
    username
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
    problemsSolvedBeatsStats {
      difficulty
      percentage
    }
  }
}
""" % LEETCODE_USERNAME

HEADERS = {"Content-Type": "application/json"}

# Fetch data from LeetCode
response = requests.post(LEETCODE_API_URL, json={"query": QUERY}, headers=HEADERS)
data = response.json()

if "errors" in data:
    print("Error fetching data. Check username or API availability.")
    exit()

# Extracting relevant data
submission_stats = data["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
total_solved = sum(item["count"] for item in submission_stats)  # Total problems solved
streak = "XX"  # LeetCode API does not directly provide streak data

# Placeholder for detailed problem log (you can extend this to fetch problem details)
problem_log = """
| Date       | Problem | Difficulty | Solution |
|------------|---------|------------|----------|
| YYYY-MM-DD | [Example Problem](https://leetcode.com/problems/) | Easy | [Solution](./solutions/example.py) |
"""

# Generate progress.md content
progress_md = f"""# LeetCode Progress Tracker 📈

This file dynamically tracks my solved problems.

## 📅 Daily Log
{problem_log}

---

## 📊 Summary
- ✅ **Total Problems Solved:** {total_solved}
- 🔥 **Current Streak:** {streak} Days
- 📌 **Topics Covered:** Arrays, Strings, Linked Lists, Dynamic Programming, etc.

Keep grinding! 🚀
"""

# Save to progress.md
with open("progress.md", "w") as f:
    f.write(progress_md)

print("✅ Progress updated successfully!")
