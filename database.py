

from sqlalchemy import create_engine, text
import pymysql
from dotenv import load_dotenv
import os
import json

# Load the environment variables from the .env file
load_dotenv()

# Get the password from the environment variable
connection_str = os.environ.get('CONNECTION_STRING')


ssl_args = {'ssl': {"ssl_cert": "/etc/ssl/cert.pem"}}
engine = create_engine(
    connection_str,
    connect_args=ssl_args
)


def get_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for res in result.all():
            jobs.append(res._asdict())

        return jobs


def get_job(id):
    with engine.connect() as conn:
        query = f"select * from jobs where id={id} "
        result = conn.execute(text(query))
        # print(type(result.all()[0]))
        
        rows = result.all()
        if len(rows):
            return rows[0]._asdict()
        else:
            return None

       

