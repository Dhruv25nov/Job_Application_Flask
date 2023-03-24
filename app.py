from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru",
        "salary": 2100000
    },
    {
        "id": 1,
        "title": "Data Scientist",
        "location": "Bengaluru",
        "salary": 3100000
    },
    {
        "id": 1,
        "title": "Automation Engineer",
        "location": "Noida",
        "salary": 2100000
    },
    {
        "id": 1,
        "title": "Big Data Engineer",
        "location": "Bengaluru",
        "salary": 4000000
    }
]

company_name = "Jovian"


@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS, portal_name=company_name)

@app.route("/api/jobs")
def jobs_data():
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
