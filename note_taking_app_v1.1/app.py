from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Sample database for demonstration
users = {"user": "user"}
notes = {}

# Session timeout (in seconds)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

@app.route('/', methods=["GET", "POST"])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        action = request.form.get("action")
        if action == "Add":
            note_name = request.form.get("note_name")
            note_description = request.form.get("note_description")
            if note_name in notes:
                return render_template("home.html", notes=notes, error="Note name already exists. Try saving with a different name.")
            notes[note_name] = {"description": note_description, "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        elif action == "Edit":
            note_name = request.form.get("note_name")
            new_note_name = request.form.get("new_note_name")
            new_note_description = request.form.get("new_note_description")
            if new_note_name != note_name and new_note_name in notes:
                return render_template("home.html", notes=notes, error="Note name already exists. Try saving with a different name.")
            notes[new_note_name] = {"description": new_note_description, "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            if new_note_name != note_name:
                del notes[note_name]
        elif action == "Delete":
            delete_note_name = request.form.get("delete_note_name")
            if delete_note_name in notes:
                del notes[delete_note_name]
            else:
                return render_template("home.html", notes=notes, error="Note not found.")

    return render_template("home.html", notes=notes)

@app.route('/login', methods=["GET", "POST"])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
