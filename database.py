

from sqlalchemy import create_engine, text
import pymysql
from dotenv import load_dotenv
import os


# Load the environment variables from the .env file
load_dotenv()

# Get the password from the environment variable
connection_str = os.environ.get('CONNECTION_STRING')

# Ssl certificate path
ssl_args = {'ssl': {"ssl_cert": "/etc/ssl/cert.pem"}}

engine = create_engine(
    connection_str,
    connect_args=ssl_args
)

# Function to fetch all jobs from database


def get_jobs():
    with engine.connect() as conn:
        query = text("select * from jobs")
        result = conn.execute(query)

        jobs = []
        for row in result.all():
            jobs.append(row._asdict())

        return jobs

# Function to get a particular job matching id from database


def get_job(id):
    with engine.connect() as conn:
        query = text("select * from jobs where id= :id_value ")
        params = {
            "id_value": id
        }
        result = conn.execute(query, params)

        rows = result.all()
        if len(rows):
            return rows[0]._asdict()
        else:
            return None

# Function to submit job application


def feed_application(id, data):
    with engine.connect() as conn:
        query = text("""insert into applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
                        values(:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)""")
        params = {
            "job_id": id,
            "full_name": data["name"],
            "email": data["email"],
            "linkedin_url": data["linkedin"],
            "education": data["education"],
            "work_experience": data["experience"],
            "resume_url": data["resume"]
        }
        conn.execute(query, params)
