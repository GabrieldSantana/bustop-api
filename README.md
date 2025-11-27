# BuStop API

Este projeto utilizan **Python + FastAPI**,
do Bustop

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   **Python 3.10+**
-   **FastAPI**
-   **Motor (MongoDB async driver)**
-   **Uvicorn**
-   **Pydantic**
-   **Python-dotenv**

------------------------------------------------------------------------

## 📁 Estrutura de Pastas

    bustop_api/
    ├─ app/
    │  ├─ main.py
    │  ├─ config.py
    │  ├─ deps.py
    │  ├─ routes/
    │  │  └─ leitura_router.py
    │  ├─ controllers/
    │  │  └─ leitura_controller.py
    │  ├─ services/
    │  │  └─ leitura_service.py
    │  ├─ repositories/
    │  │  └─ leitura_repository.py
    │  ├─ schemas/
    │  │  └─ leitura_schema.py
    │  ├─ utils/
    │  │  └─ errors.py
    ├─ requirements.txt
    ├─ .env.example
    ├─ .gitignore
    └─ README.md

------------------------------------------------------------------------

## ⚙️ Instalação e Uso

### 1. Criar ambiente virtual

``` bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate       # Windows
```

### 2. Instalar dependências

``` bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Crie um arquivo `.env` baseado em `.env.example`:

    MONGO_URI=mongodb+srv://<user>:<password>@<cluster>.mongodb.net/
    MONGO_DB=brtiot
    ORIGINS=http://localhost:3000
    API_PORT=8080

### 4. Rodar o servidor

``` bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

------------------------------------------------------------------------

## 📡 Endpoints

### `GET /`

Retorna status da API.

### `POST /api/dados`

Cria uma nova leitura:

``` json
{
  "temperatura": 25,
  "umidade": 55,
  "pessoas": 2
}
```

### `GET /api/dados?limit=100`

Lista as leituras registradas.

------------------------------------------------------------------------

## 📘 Documentação Automática

FastAPI gera automaticamente:

-   Swagger UI → `http://localhost:8080/docs`
-   ReDoc → `http://localhost:8080/redoc`

------------------------------------------------------------------------

## 🔒 Melhorias Implementadas

-   Código totalmente assíncrono
-   Validação forte com Pydantic
-   Estrutura escalável com camadas (controller/service/repository)
-   Conexão MongoDB utilizando pooling do Motor
-   Variáveis sensíveis movidas para `.env`
-   Logging padronizado
-   Documentação gerada automaticamente
-   CORS configurado corretamente
-   Estrutura limpa, tipada e seguindo PEP8

------------------------------------------------------------------------

## 🛠 Requisitos

-   Python 3.10+
-   MongoDB Atlas ou servidor Mongo compatível
