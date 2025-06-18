# test_app.py
import pytest
from app import app


@pytest.fixture  # Cria um contexto de teste (client da API)
def client():
    app.config["TESTING"] = True  # Configura app em modo teste
    with app.test_client() as client:  # Cria cliente para simular requisições
        yield client  # Disponibiliza o cliente para os testes


def test_saudacao_endpoint(client):
    # Arrange - preparação já feita pela fixture

    # Act - chamada ao endpoint
    resposta = client.get("/saudacao/Maria")  # Simula requisição GET

    # Assert - verificações
    assert resposta.status_code == 200  # Verifica código HTTP
    assert resposta.json == {"mensagem": "Olá, Maria!"}  # Verifica corpo da resposta
