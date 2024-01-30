from flask import Flask, render_template, request,redirect,url_for,session,flash
app = Flask(__name__)
app.secret_key = 'myfirstapp'

@app.route("/")
def ind():
    return render_template("login.html")

@app.route("/loginverify",methods=["post"])
def loginverify():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if username == "admin" and password == "admin":
        session["name"] = username
        flash("Login successful!")
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("ind"))

@app.route("/dashboard")
def dashboard():
    if "name" in session and session["name"] != None and session["name"] != "":
      username = session["name"]
      return render_template("dashboard.html",name=username)
    else:
        flash("Invalid username or password")
        return redirect(url_for("ind"))

@app.route("/logout")
def logout():
    session.pop("name",None)
    flash("You have been logged out!")
    return redirect(url_for("ind"))


if __name__=='__main__':
    app.run(debug=True)