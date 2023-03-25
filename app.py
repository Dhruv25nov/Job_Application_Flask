from flask import Flask, render_template, jsonify
from database import get_jobs


app = Flask(__name__)


company_name = "Jovian"
jobs_list = get_jobs()


@app.route("/")
def hello():
    return render_template("home.html", jobs=jobs_list, portal_name=company_name)
    # print(type(jobs_list))


@app.route("/api/jobs")
def jobs_data():

    return jsonify(jobs_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
