import flask
import os
import csv
import random
import datetime
import json
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
        if (len(linha) == 3) and (linha[2] != "Família"):
            termos.append(linha[1])
    return termos

def definir_saudacao():
    hora_atual = datetime.datetime.now().hour
    if (hora_atual >= 0 and hora_atual < 6): return "Boa madrugada"
    elif (hora_atual >= 6 and hora_atual < 12): return "Bom dia"
    elif (hora_atual >= 12 and hora_atual < 18): return "Boa tarde"
    else: return "Boa noite"

termos = buscar_termos_validos()

@app.route("/random-greeting")
def buscar_saudacao_aleatoria():
    numero_randomico = random.randint(1, len(termos))
    cumprimento = definir_saudacao() + ", meu " + termos[numero_randomico]
    response = {"cumprimento": cumprimento}
    return json.dumps(response, ensure_ascii=False).encode('utf8')

if __name__=='__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
