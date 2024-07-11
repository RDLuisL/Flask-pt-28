from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    if(request.method=='GET'):
        return render_template("index.html")
    elif(request.method=='POST'):
        return jsonify({
            "mensaje": "Este es un mensaje dentro de un json"
        })
    else:
        return "deleted"

@app.route("/ping", methods=['GET'])
def pingpong():
    body = request.get_json()
    response = {
        "mesange": body['nombre'] + " ha decidido jugar ping pong"        
    }
    return jsonify(response)

@app.route("/saludar/<nombre>", methods=['GET'])
def saludar(nombre):
    return "Hola! "+ nombre


app.run(host= '0.0.0.0', debug=True)