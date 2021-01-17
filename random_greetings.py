import flask
import os
import csv
import random

from flask import Flask

app = Flask(__name__)

def abrir_csv():
    nome_arquivo_cbo = 'cbo/lista.csv'
    arquivo_csv = open(nome_arquivo_cbo, newline='')
    return csv.reader(arquivo_csv, delimiter=',')

def buscar_termos_validos():
    arquivo_csv = abrir_csv()
    termos = []
    for linha in arquivo_csv:
        if ((len(linha) == 3) and (linha[2] != "Família")):
            termos.append(linha[1])
    return termos

# def normalizar_termo():
#     return ""

termos = buscar_termos_validos()

@app.route("/random-greeting")
def get_random_greeting():
    numero_randomico = random.randint(1, len(termos))
    return "Boa noite, meu " + termos[numero_randomico]

if __name__=='__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
