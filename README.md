# Job_Application

This is a WebApp made using Flask.

## About

>Job Application App is a mimic  of Job Portals

## What a admin can do?

- Add new jobs to the portal
- See details of the applicants

## What you applicant can do?

- Navigate and apply for jobs listed

## Languages, Libraries and Tools used

- Flask
- Jinja
- SqlAlchemy
- MySql WorkBench (Loca Mysql client)
- Planet Scale (Free Mysql cloud database)
- Python
- Bootstrap
- Html

## Steps to run the app at local system

1. Clone the repository
2. Run `pip install -r requirement.txt`
3. Create .env file and store CONNECTION_STRING with your details obtained from PLanet Scale Database after creating a account on it
4. CONNECTION_STRING = "mysql+pymysql://<db_user>:<db_password>@tcp(<db_host>:<db_port>)/<db_name>?charset=utf8mb4"
5. Run `python app.js`
6. Go to  [http://localhost:5000/](http://localhost:5000/)

Deployed : <https://jobapplication-4tmz.onrender.com>
