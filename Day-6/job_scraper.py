import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://realpython.github.io/fake-jobs/"

# Skills we want to detect
skills_to_check = [
    "Python",
    "JavaScript",
    "Java",
    "HTML",
    "CSS",
    "Django",
    "Flask",
    "SQL",
    "React",
    "Node.js",
    "PHP",
    "Ruby",
    "AWS",
    "Docker",
    "Git",
    "Selenium",
    "Playwright",
    "Scrapy",
    "Pandas",
    "NumPy"
]


def extract_skills(description):
    found_skills = []

    for skill in skills_to_check:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, description, re.IGNORECASE):
            found_skills.append(skill)

    return ", ".join(found_skills)


response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

job_data = []


for job in jobs:

    title = job.find("h2", class_="title").get_text(strip=True)

    company = job.find("h3", class_="company").get_text(strip=True)

    location = job.find("p", class_="location").get_text(strip=True)

    link = job.find("a", string="Apply")

    job_url = link.get("href") if link else ""

    description = ""

    if job_url:

        job_response = requests.get(job_url)
        job_response.raise_for_status()

        job_soup = BeautifulSoup(job_response.text, "html.parser")

        description_section = job_soup.find("div", class_="content")

        if description_section:
            description = description_section.get_text(" ", strip=True)

    # Extract actual skills from description
    skills = extract_skills(description)

    job_data.append({
        "title": title,
        "company": company,
        "location": location,
        "skills": skills,
        "salary": "Not available",
        "url": job_url
    })


# Save data to CSV
with open("jobs.csv", "w", newline="", encoding="utf-8") as file:

    fieldnames = [
        "title",
        "company",
        "location",
        "skills",
        "salary",
        "url"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(job_data)


print("Scraping completed!")
print("Total jobs:", len(job_data))
print("Data saved to jobs.csv")
