# FastAPI Python Project README

Este é o README para o seu projeto em Python usando FastAPI, com um endpoint em /mqtt.

## Requisitos do Sistema

Certifique-se de ter os seguintes requisitos instalados em seu sistema:

- Python 3.6 ou superior
- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [mqtt](https://pypi.org/project/paho-mqtt/)

## Instalação

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/macgyvercsehdev/tcc-api-mqtt
cd tcc-api-mqtt
```

Crie um ambiente virtual (recomendado, mas opcional):

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- No Linux/macOS:
  ```bash
  source venv/bin/activate
  ```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Configuração

Configure as variáveis de ambiente no arquivo `.env`:
> Lembrando que deve estar na raiz do projeto

```dotenv
MQTT_BROKER=mqtt://seu-broker-url
MQTT_PORT=sua-porta
```

## Executando o Projeto

Certifique-se de ter ativado o ambiente virtual (se estiver usando) e configurado as variáveis de ambiente.

Execute o projeto usando o Uvicorn:

```bash
uvicorn main:app --reload
```

O projeto estará disponível em http://localhost:8000.

## Testando o Endpoint /mqtt

Acesse a ferramenta com o POSTMAN ou outro software que suporte http request para testar o endpoint:

```bash
Adicione a url: http://localhost:8000/mqtt e faça sua requisição
```

Isso enviará uma requisição para o endpoint /mqtt usando o método GET.

Lembre-se de ajustar as mensagens e payloads de acordo com os requisitos do projeto.

## Contribuindo

Se você quiser contribuir para este projeto, por favor, abra uma [issue](https://github.com/macgyvercsehdev/tcc-api-mqtt/issues) ou envie um [pull request](https://github.com/macgyvercsehdev/tcc-api-mqtt/pulls).

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).