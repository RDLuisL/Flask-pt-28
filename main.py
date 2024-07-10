from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():
    if(request.method=='GET'):
        return render_template("index.html")
    else:
        return jsonify({
            "mensaje": "Este es un mensaje dentro de un json"
        })

app.run(host= '0.0.0.0')