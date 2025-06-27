import pytest
from exercicio.app import app

#  Cliente de teste configurado com o Flask
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


#  Testa listagem de tarefas (GET /tarefas)
def test_listar_tarefas(client):
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0


#  Testa criação de nova tarefa com sucesso (POST /tarefas)
def test_criar_tarefa_sucesso(client):
    nova_tarefa = {"tarefa": "Aprender pytest", "feito": False}
    response = client.post("/tarefas", json=nova_tarefa)

    assert response.status_code == 201
    dados = response.json
    assert isinstance(dados, dict)
    assert dados["tarefa"] == "Aprender pytest"
    assert dados["feito"] is False
    assert "id" in dados


#  Testa criação de tarefa com campos faltando
def test_criar_tarefa_campos_faltando(client):
    response = client.post("/tarefas", json={"tarefa": "Sem feito"})
    assert response.status_code == 400
    assert "erro" in response.json


#  Testa criação de tarefa com tipos inválidos
def test_criar_tarefa_tipos_invalidos(client):
    dados_invalidos = {"tarefa": 123, "feito": "não é booleano"}
    response = client.post("/tarefas", json=dados_invalidos)
    assert response.status_code == 400
    assert "erro" in response.json


#  Testa obtenção de tarefa existente
def test_obter_tarefa_existente(client):
    response = client.get("/tarefas/1")
    assert response.status_code == 200
    assert response.json["id"] == 1


# Testa obtenção de tarefa inexistente
def test_obter_tarefa_inexistente(client):
    response = client.get("/tarefas/9999")
    assert response.status_code == 404
    assert "erro" in response.json


# Testa atualização de tarefa existente
def test_atualizar_tarefa_existente(client):
    atualizacao = {"tarefa": "Atualizada", "feito": True}
    response = client.put("/tarefas/1", json=atualizacao)

    assert response.status_code == 200
    dados = response.json
    assert dados["tarefa"] == "Atualizada"
    assert dados["feito"] is True


# Testa atualização de tarefa inexistente
def test_atualizar_tarefa_inexistente(client):
    atualizacao = {"tarefa": "Qualquer", "feito": True}
    response = client.put("/tarefas/9999", json=atualizacao)

    assert response.status_code == 404
    assert "erro" in response.json


# Testa remoção de tarefa existente
def test_remover_tarefa_existente(client):
    response = client.delete("/tarefas/1")
    assert response.status_code == 200
    assert "mensagem" in response.json

    # Confirma que foi removida
    response_get = client.get("/tarefas/1")
    assert response_get.status_code == 404


# remoção de tarefa inexistente
def test_remover_tarefa_inexistente(client):
    response = client.delete("/tarefas/9999")
    assert response.status_code == 404
    assert "erro" in response.json

#pytest -v