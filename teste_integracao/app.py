# app.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/saudacao/<nome>")
def saudacao(nome):
    return jsonify({"mensagem": f"Olá, {nome}!"})
