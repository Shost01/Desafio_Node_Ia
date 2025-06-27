# 🧩 Desafio_Node_Ia

> Um projeto de arquitetura modular com foco em testes robustos e boas práticas de engenharia de software, integrando conceitos de IA.

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Test Coverage](https://img.shields.io/badge/tests-100%25-success)]()

---

## 📖 Visão Geral

O **Desafio_Node_Ia** é uma aplicação backend focada em qualidade de código, testes automatizados e estrutura limpa, modelada sob padrões sólidos de design. Embora inicialmente pensado como um projeto Node.js, a solução atual utiliza **Python** para implementação de rotinas críticas (possivelmente ligadas à IA), mantendo o foco em arquitetura desacoplada e testável.

---

## 🧱 Arquitetura do Projeto

```
Desafio_Node_Ia/
│
├── app/                      # Código-fonte da aplicação
│   ├── models/               # Modelos de dados (ex: Product)
│   ├── repositories/         # Regras de acesso a dados
│   └── controllers/          # Camada de controle (orquestração de regras)
│
├── tests/                    # Testes unitários organizados por camada
│   ├── test_product_model.py
│   ├── test_product_repository.py
│   └── test_product_controller.py
│
├── run.py                    # Entry point da aplicação
├── requirements.txt          # Dependências Python
└── venv/                     # Ambiente virtual isolado (não versionado)
```

---

## 🧪 Filosofia de Testes

Testes não são acessórios — são infraestrutura. Toda modificação passa por testes de regressão. Este projeto cobre:

| Camada       | Arquivo                      | Objetivo                                                                 |
|--------------|------------------------------|--------------------------------------------------------------------------|
| 🧬 Model      | `test_product_model.py`       | Valida estrutura de dados e atributos esperados                         |
| 📦 Repository | `test_product_repository.py`  | Testa persistência simulada e CRUD isolado                              |
| 🎛 Controller | `test_product_controller.py`  | Verifica injeção de dependências e roteamento de chamadas               |

Cada teste é projetado para **detecção precoce de falhas**, **refatoração segura** e **legibilidade a longo prazo**.

---

## ✅ Execução Local

### 1. Clone o projeto

```bash
git clone https://github.com/Shost01/Desafio_Node_Ia.git
cd Desafio_Node_Ia
```

### 2. Crie e ative o ambiente virtual

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute os testes

```bash
pytest tests/
```

---

## 🧬 Exemplo de Teste (Modelo)

```python
def test_product_creation():
    product = Product(
        id=1,
        name="Produto Teste",
        description="Descrição teste",
        price=10.0,
        category="Categoria Teste",
        stock=5
    )
    assert product.name == "Produto Teste"
    assert product.price == 10.0
    assert product.stock == 5
```

---

## 🛣️ Roadmap e Melhorias Futuras

- [ ] Integração com banco de dados real (SQLite/PostgreSQL)
- [ ] Implementação de API REST com FastAPI ou Express.js
- [ ] Cobertura com testes de integração
- [ ] Testes End-to-End com `pytest` + `httpx`
- [ ] Deploy com Docker e GitHub Actions

---

## 🙋 Contribuição

Quer contribuir? Excelente! Segue o fluxo:

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nome-da-funcionalidade`
3. Escreva código limpo, com testes cobrindo o que for novo
4. Faça o push e crie um Pull Request

---

## 📎 Referência

- 📂 Repositório oficial: [Shost01/Desafio_Node_Ia](https://github.com/Shost01/Desafio_Node_Ia)

---

## 📜 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar, modificar e compartilhar!
