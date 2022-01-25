from flask import *

app = Flask(__name__)
app.secret_key = "ABCDEFG"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/Home')
def homepage():
    return render_template("index.html")


@app.route("/Login", methods=['GET', 'POST'])
def Login():
    if request.method == "POST":
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
        return f"<h1>{user}<h1>"
    else:
        return redirect(url_for("Login"))


@app.route("/Logout")
def Logout():
    session.pop("user", None)
    return redirect(url_for("Login"))


@app.route("/Disabled")
def Disabled():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
