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



# @app.route('/skills')



# @app.route('/experience')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')