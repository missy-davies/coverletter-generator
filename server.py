"""A cover letter generator"""

from flask import Flask, render_template, request 

app = Flask(__name__)

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

    return render_template("job.html")


@app.route('/skills')
def get_skills():
    """Get information about skills"""

    return render_template("skills.html")


@app.route('/experience')
def get_experience():
    """Get information about experience"""

    return render_template("experience.html")


@app.route('/education')
def get_education():
    """Get information about education"""

    return render_template("education.html")


@app.route('/cover-letter')
def generate_coverletter():
    """Generate custom cover letter"""

    return render_template("cover-letter.html")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')