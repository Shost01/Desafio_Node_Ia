# Documentação dos Testes Unitários do Projeto

## Estrutura dos Testes

Os testes estão organizados na pasta `tests/`, com um arquivo para cada camada principal do projeto:

- `test_product_model.py` — Testa a camada Model (`Product`)
- `test_product_repository.py` — Testa a camada Repository (`ProductRepository`)
- `test_product_controller.py` — Testa a camada Controller (`ProductController`)

---

## 1. Teste do Model (`Product`)

**Arquivo:** `tests/test_product_model.py`

**Descrição:**
Testa se a classe `Product` está criando objetos corretamente com todos os atributos obrigatórios.

**Exemplo de teste:**
```python
def test_product_creation():
    product = Product(
        id=1,
        name='Produto Teste',
        description='Descrição teste',
        price=10.0,
        category='Categoria Teste',
        stock=5
    )
    assert product.id == 1
    assert product.name == 'Produto Teste'
    assert product.description == 'Descrição teste'
    assert product.price == 10.0
    assert product.category == 'Categoria Teste'
    assert product.stock == 5
```

**Validação:**
Garante que todos os atributos do produto são atribuídos corretamente ao instanciar a classe.

---

## 2. Teste do Repository (`ProductRepository`)

**Arquivo:** `tests/test_product_repository.py`

**Descrição:**
Testa se o repositório consegue criar e armazenar um produto corretamente usando o método `create`.

**Exemplo de teste:**
```python
def test_create_product():
    repo = ProductRepository()
    product = repo.create(
        name='Produto Teste',
        description='Descrição teste',
        price=10.0,
        category='Categoria Teste',
        stock=5
    )
    assert product.id is not None
    assert product.name == 'Produto Teste'
    assert product.description == 'Descrição teste'
    assert product.price == 10.0
    assert product.category == 'Categoria Teste'
    assert product.stock == 5
```

**Validação:**
Garante que o método `create` do repositório está funcionando e que o produto criado tem os atributos corretos.

---

## 3. Teste do Controller (`ProductController`)

**Arquivo:** `tests/test_product_controller.py`

**Descrição:**
Testa se o controller é instanciado corretamente e possui o atributo `repository`.

**Exemplo de teste:**
```python
def test_controller_has_repository():
    controller = ProductController()
    assert hasattr(controller, 'repository')
```

**Validação:**
Garante que o controller está corretamente configurado para acessar o repositório de produtos.

---

## Como rodar os testes

1. Instale o pytest (se ainda não instalou):
   ```bash
   pip install pytest
   ```

2. Execute os testes com:
   ```bash
   export PYTHONPATH=$(pwd) && pytest
   ```
   (No Windows cmd use: `set PYTHONPATH=%CD% && pytest`)

---

## Referências

- [Documentação oficial do pytest](https://docs.pytest.org/)
- [Testes unitários em Python — Real Python](https://realpython.com/python-testing/)
- [Como organizar testes em projetos Python](https://docs.python-guide.org/writing/tests/)
