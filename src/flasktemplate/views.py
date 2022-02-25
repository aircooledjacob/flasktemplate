from flasktemplate import app
from flask import render_template, request


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', url=request.url), 404


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=["GET", "POST"])
def log_in():
    if request.method == "GET": return render_template('login.html')
    if request.method == "POST":
        return "almost there"


@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('register.html')
