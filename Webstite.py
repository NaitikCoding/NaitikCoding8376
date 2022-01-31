from flask import *
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "ABCDEFG"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/Home')
def homepage():
    return render_template("index.html")


@app.route("/Login", methods=['GET', 'POST'])
def Login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("User"))
    else:
        if "user" in session:
            return redirect(url_for("User"))
        return render_template("login.html")


@app.route("/User")
def User():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", content="user")
    else:
        return redirect(url_for("Login"))


@app.route("/Logout")
def Logout():
    session.pop("user", None)
    return redirect(url_for("Login"))


if __name__ == '__main__':
    app.run(debug=True)
