"""A cover letter generator"""

from flask import Flask, request, render_template, redirect, session
import jinja2


app = Flask(__name__)
app.secret_key = 'THISISTHESECRETKEY'


@app.route('/')
def home_page():
    """A landing page with a call to action"""

    return render_template("home-page.html")


@app.route('/start')
def get_name():
    """Basic instructions and get user's name"""

    return render_template("start.html")


@app.route('/job')
def get_job():
    """Get information about prospective job"""

    full_name = request.args.get("full-name")
    name_list = full_name.split(" ")

    first = name_list[0].title()
    session['first'] = first

    last = name_list[1].title() 
    session['last'] = last

    return render_template("job.html")


@app.route('/skills')
def get_skills():
    """Get information about skills"""

    job_title = request.args.get("job-title").title()
    session['job-title'] = job_title

    company = request.args.get("company").title()
    session['company'] = company

    return render_template("skills.html")


@app.route('/experience')
def get_experience():
    """Get information about experience"""

    skill1 = request.args.get("skill-1").lower()
    session['skill1'] = skill1

    skill2 = request.args.get("skill-2").lower()
    session['skill2'] = skill2

    skill3 = request.args.get("skill-3").lower()
    session['skill3'] = skill3

    return render_template("experience.html")


@app.route('/education')
def get_education():
    """Get information about education"""

    years_experience = request.args.get("years-experience")
    session['years_experience'] = years_experience

    accomplishment = request.args.get("accomplishment")
    session['accomplishment'] = accomplishment

    return render_template("education.html")


@app.route('/cover-letter')
def generate_coverletter():
    """Generate custom cover letter"""

    edu = request.args.get("level-education")
    session['level-education'] = edu

    special = request.args.get("special")
    session['special'] = special

    return render_template("cover-letter.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")