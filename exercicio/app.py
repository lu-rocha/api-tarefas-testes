# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = [{"id": 1, "tarefa": "Estudar testes", "feito": False}]


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.json

    if not dados or "tarefa" not in dados or "feito" not in dados:
        return jsonify({"erro": "Campos obrigatórios: 'tarefa' e 'feito'"}), 400

    if not isinstance(dados["tarefa"], str) or not isinstance(dados["feito"], bool): #verifica o tipo
        return (
            jsonify(
                {"erro": "Tipos inválidos: 'tarefa' deve ser string e 'feito' booleano"}

            ),
            400,
        )

    dados["id"] = len(tarefas) + 1 #retorna o tamanho do obj
    tarefas.append(dados)
    return jsonify(dados), 201


@app.route("/tarefas/<int:id>", methods=["GET"])
def obter_tarefa(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if tarefa:
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    dados = request.json
    tarefa.update(dados)
    return jsonify(tarefa)


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def remover_tarefa(id):
    global tarefas
    tarefa_existente = next((t for t in tarefas if t["id"] == id), None)

    if not tarefa_existente:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tarefas = [t for t in tarefas if t["id"] != id]
    return jsonify({"mensagem": "Tarefa removida"}), 200
