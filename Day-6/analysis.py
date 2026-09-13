import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Connect to SQLite database
# --------------------------------------------------

DB_NAME = "jobs.db"

conn = sqlite3.connect(DB_NAME)

# Read jobs table into pandas
df = pd.read_sql_query("SELECT * FROM jobs", conn)

conn.close()

print("Dataset loaded successfully!")
print(f"Total jobs: {len(df)}")
print("\nColumns:")
print(df.columns.tolist())


# --------------------------------------------------
# 2. Chart 1 - Most In-Demand Skills
# --------------------------------------------------

# Remove missing skills
skills = df["skills"].dropna()

# Split skills such as:
# "Python, HTML, CSS, Django"
skill_list = []

for skill_string in skills:
    for skill in skill_string.split(","):
        skill = skill.strip()

        if skill:
            skill_list.append(skill)

# Count each skill
skill_counts = pd.Series(skill_list).value_counts().head(10)

plt.figure(figsize=(10, 6))

skill_counts.sort_values().plot(
    kind="barh"
)

plt.title("Most In-Demand Skills")
plt.xlabel("Number of Jobs")
plt.ylabel("Skill")
plt.tight_layout()

plt.savefig("most_in_demand_skills.png")
plt.show()


# --------------------------------------------------
# 3. Chart 2 - Jobs by Location
# --------------------------------------------------

location_counts = (
    df["location"]
    .dropna()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))

location_counts.sort_values().plot(
    kind="barh"
)

plt.title("Jobs by Location")
plt.xlabel("Number of Jobs")
plt.ylabel("Location")
plt.tight_layout()

plt.savefig("jobs_by_location.png")
plt.show()


# --------------------------------------------------
# 4. Chart 3 - Jobs by Company
# --------------------------------------------------

company_counts = (
    df["company"]
    .dropna()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))

company_counts.sort_values().plot(
    kind="barh"
)

plt.title("Top Companies by Number of Job Listings")
plt.xlabel("Number of Jobs")
plt.ylabel("Company")
plt.tight_layout()

plt.savefig("jobs_by_company.png")
plt.show()


# --------------------------------------------------
# 5. Print analysis summary
# --------------------------------------------------

print("\n--- Analysis Summary ---")

print("\nTop 10 Skills:")
print(skill_counts)

print("\nTop 10 Locations:")
print(location_counts)

print("\nTop 10 Companies:")
print(company_counts)

print("\nAnalysis completed successfully!")
