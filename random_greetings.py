import flask
import os
import csv
import random
import json
import datetime
from pytz import timezone
from flask import Flask

app = Flask(__name__)

def abrir_csv(nome_arquivo):
    arquivo_csv = open(nome_arquivo, newline='')
    return csv.reader(arquivo_csv, delimiter=',')

def buscar_termos_validos(arquivo_csv):
    termos = []
    for linha in arquivo_csv:
        if (len(linha) == 3) and (linha[2] != "Família"):
            termos.append(linha[1])
    return termos

def definir_saudacao(hora_atual):
    if (hora_atual >= 0 and hora_atual < 6): return "Boa madrugada"
    elif (hora_atual >= 6 and hora_atual < 12): return "Bom dia"
    elif (hora_atual >= 12 and hora_atual < 18): return "Boa tarde"
    else: return "Boa noite"

def montar_response(cumprimento):
    response = {"cumprimento": cumprimento}
    return json.dumps(response, ensure_ascii=False).encode('utf8')

arquivo_csv = abrir_csv("cbo/lista.csv")
termos = buscar_termos_validos(arquivo_csv)

@app.route("/random-greeting")
def buscar_saudacao_aleatoria():    
    numero_randomico = random.randint(1, len(termos))
    hora_atual = datetime.datetime.now().astimezone(timezone('America/Sao_Paulo')).hour
    cumprimento = definir_saudacao(hora_atual) + ", meu " + termos[numero_randomico]
    return montar_response(cumprimento)

if __name__=='__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
