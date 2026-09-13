import csv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# Create SQLite database
engine = create_engine("sqlite:///jobs.db")

Base = declarative_base()


# Define the jobs table
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    skills = Column(String)
    salary = Column(String)
    url = Column(String)


# Create the table
Base.metadata.create_all(engine)


# Create database session
Session = sessionmaker(bind=engine)
session = Session()


# Read jobs.csv
with open("jobs.csv", "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        job = Job(
            title=row["title"],
            company=row["company"],
            location=row["location"],
            skills=row["skills"],
            salary=row["salary"],
            url=row["url"]
        )

        session.add(job)


# Save all jobs
session.commit()

print("Database created successfully!")
print("Jobs inserted:", session.query(Job).count())

session.close()
