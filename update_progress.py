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
    recentAcSubmissionList {
      title
      titleSlug
      timestamp
      difficulty
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

# Extracting problem-solving stats
submission_stats = data["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
total_solved = sum(item["count"] for item in submission_stats)  # Total problems solved

# Extracting recent submissions
recent_problems = data["data"]["matchedUser"]["recentAcSubmissionList"]

# Formatting problem log dynamically
problem_log = """
| Date       | Problem | Difficulty | Solution |
|------------|---------|------------|----------|
"""

for problem in recent_problems:
    date_solved = datetime.utcfromtimestamp(int(problem["timestamp"])).strftime("%Y-%m-%d")
    problem_name = problem["title"]
    problem_slug = problem["titleSlug"]
    difficulty = problem["difficulty"]
    solution_link = f"./solutions/{problem_slug}.py"  # Assuming solutions are stored in /solutions

    problem_log += f"| {date_solved} | [{problem_name}](https://leetcode.com/problems/{problem_slug}/) | {difficulty} | [Solution]({solution_link}) |\n"

# Generate progress.md content
progress_md = f"""# LeetCode Progress Tracker 📈

This file dynamically tracks my solved problems.

## 📅 Daily Log
{problem_log}

---

## 📊 Summary
- ✅ **Total Problems Solved:** {total_solved}
- 🔥 **Current Streak:** XX Days (Manually Update or Automate)
- 📌 **Topics Covered:** Arrays, Strings, Linked Lists, Dynamic Programming, etc.

Keep grinding! 🚀
"""

# Save to progress.md
with open("progress.md", "w") as f:
    f.write(progress_md)

print("✅ Progress updated successfully!")
