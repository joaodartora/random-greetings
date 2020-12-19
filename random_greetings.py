import flask
import os
from flask import Flask

app = Flask(__name__)

@app.route("/random-greeting")
def get_random_greeting():
    return "Boa noite meu Abacaxicultor"

if __name__=='__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')