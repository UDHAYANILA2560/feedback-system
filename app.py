from flask import Flask, render_template, request, redirect, url_for, session 
import sqlite3
from model import analyze_feedback
app = Flask(__name__)
app.secret_key = "secret123"
# Function to connect database
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn
# -------------------------
# Login Page
# -------------------------
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        student_id = request.form["student_id"]
        password = request.form["password"]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM student WHERE id=? AND password=?",
            (student_id, password)
        )
        student = cursor.fetchone()
        conn.close()

        if student:
            return redirect(url_for("feedback", student_id=student_id))
        else:
            return "Invalid Login"

    return render_template("login.html")
# -------------------------
# Admin Login
# -------------------------
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "uvsquare" and password == "uvv1234":
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            return render_template("admin_login.html", error="Invalid Login")

    return render_template("admin_login.html")
# -------------------------
# Feedback Page
# -------------------------
@app.route("/feedback/<student_id>", methods=["GET", "POST"])
def feedback(student_id):
    if request.method == "POST":
        text = request.form["feedback"]
        suggestion = request.form.get("suggestion")  
        sentiment = analyze_feedback(text)
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (student_id, text, sentiment, suggestion) VALUES (?, ?, ?, ?)",
            (student_id, text, sentiment, suggestion)
        )
        conn.commit()
        conn.close()
        return render_template("result.html", sentiment=sentiment)
    return render_template("feedback.html")
# -------------------------
# Admin Dashboard
# -------------------------
@app.route("/admin")
def admin():

    # 🔒 Protect admin page
    if "admin" not in session:
        return redirect(url_for("admin_login"))

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT student_id, text, sentiment, suggestion FROM feedback")
    feedbacks = cursor.fetchall()

    conn.close()

    return render_template("admin.html", feedbacks=feedbacks)
   
# -------------------------
# Logout
# -------------------------
@app.route("/logout")
def logout():
    session.clear()   # clears admin session
    return redirect(url_for("login"))

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
