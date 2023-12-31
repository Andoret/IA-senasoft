from flask import Flask,request,jsonify,render_template

import function
from function import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['GET','POST'])
def translate():  # put application's code here
    data = request.get_json()
    url= data.get('url',0)
    resultado= function.deteccion(url)
    return jsonify({"resultado": resultado})


if __name__ == '__main__':
    app.run(debug=True)


