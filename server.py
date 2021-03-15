"""A cover letter generator"""


from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension


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
    last = name_list[1].title() # might be extra and can remove 

    return render_template("job.html", first=first)


@app.route('/skills')
def get_skills():
    """Get information about skills"""

    position = request.args.get("job-title")

    return render_template("skills.html", position=position)


@app.route('/experience')
def get_experience():
    """Get information about experience"""

    company = request.args.get("company")

    return render_template("experience.html", company=company)


@app.route('/education')
def get_education():
    """Get information about education"""

    return render_template("education.html")


@app.route('/cover-letter')
def generate_coverletter():
    """Generate custom cover letter"""

    return render_template("cover-letter.html")



if __name__ == '__main__':
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')