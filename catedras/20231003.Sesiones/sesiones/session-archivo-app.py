from flask import Flask, session, request, render_template, redirect, url_for
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    tareas = []
    if 'tareas' in session:
        tareas = session["tareas"].split("###")
    return render_template("tareas.html", tareas=tareas)

@app.route('/tareas', methods=['POST'])
def tareas():
    if "tareas" in session:
        session['tareas'] = session["tareas"] + "###" + request.form['tarea']
    else:
        session['tareas'] = request.form['tarea']

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)


