from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ganesh@localhost/registerationsdb'
db.init_app(app)

app.secret_key = "development-key"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            return redirect(url_for('home'))

    elif request.method == "GET":
        return render_template('signup.html', form=form)


@app.route('/home')
def home():
    return 'Welcome Home'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
