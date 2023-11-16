from flask import Flask, request, make_response
  
app = Flask(__name__)
app.config['DEBUG'] = True
  
@app.route('/')
def contador_visitas():
    # Convertir valor str a entero
    # si no viene la cookie, se asume 0
    count = int(request.cookies.get('contador visitas', 0))
    # incrementar contador
    count = count + 1
    output = 'Usted ha visitado esta página ' + str(count) + ' veces'
    resp = make_response(output)
    resp.set_cookie('contador visitas', str(count))
    return resp
  
@app.route('/get')
def get_contador_visitas():
    count = request.cookies.get('contador visitas', 0)
    resp = make_response(str(count))
    return resp
  
app.run()


