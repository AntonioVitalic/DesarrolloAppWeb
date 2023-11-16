from flask import Flask, make_response, render_template
import subprocess
  
app = Flask(__name__)
  
@app.route('/ajax', methods = ['GET'])
def ajax():
    output = subprocess.run("/usr/bin/top -l 1", shell=True, capture_output=True, text=True)
    resp = make_response(output.stdout)
    resp.headers["Content-type"] = "text/plain; charset=UTF-8"
    resp.headers["Cache-Control"] = "no-cache"
    return resp

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/yui', methods = ['GET'])
def yui():
    return render_template('index-yui.html')

@app.route('/jquery', methods = ['GET'])
def jquery():
    return render_template('index-jquery.html')
  
app.run(debug=True)


