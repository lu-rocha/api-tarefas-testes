from get_currency import get_currency
from unittest.mock import patch


def test_get_temperatura_com_mock():
    # Arrange (Preparação)
    dados_mock = {  # Dados falsos que imitam a API real
        "USDBRL": {
            "code": "USD",
            "codein": "BRL",
            "name": "Dólar Americano/Real Brasileiro",
            "high": "5.5051",
            "low": "5.46065",
            "varBid": "0.0052",
            "pctChange": "0.09471",
            "bid": "5.4959",
            "ask": "5.4989",
            "timestamp": "1750194837",
            "create_date": "2025-06-17 18:13:57",
        }
    }

    # Act (Ação)
    with patch(
        "get_currency.requests.get"
    ) as mock_get:  # Substitui requests.get por um mock
        # Configura o mock:
        # 1. mock_get.return_value = objeto "resposta" falsa
        # 2. .json.return_value = define o valor retornado por resposta.json()
        mock_get.return_value.json.return_value = dados_mock

        # Chama a função original (que agora usará o mock)
        resultado = get_currency("USD-BRL")

    # Assert (Verificação)
    assert resultado == dados_mock

    # Verifica se requests.get foi chamada com a URL correta
    mock_get.assert_called_once_with(
        "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    )
