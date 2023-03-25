from flask import Flask, render_template, jsonify, request
from database import get_jobs, get_job


app = Flask(__name__)


company_name = "Jovian"
jobs_list = get_jobs()

# Home Page route


@app.route("/")
def list_all_jobs():
    return render_template("home.html", jobs=jobs_list, portal_name=company_name)


# Specific job page route


@app.route("/job/<id>")
def list_job(id):
    job = get_job(id)
    if not job:
        return "NOT FOUND! 404"
    return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=["POST"])
def job_apply(id):
    applicant_data = request.form
    job_applied = get_job(id)
   
    return render_template("application_submitted.html", applicant=applicant_data, job = job_applied)


@app.route("/api/jobs")
def jobs_data():

    return jsonify(jobs_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
