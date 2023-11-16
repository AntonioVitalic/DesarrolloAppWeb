from flask import Flask, session, request, render_template, redirect, url_for

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'940b414bb69fb679d5cd7f071a5e2012e89a6319b0e298f5b9de2eeeafbdb69f'

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

