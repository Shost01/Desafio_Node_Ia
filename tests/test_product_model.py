import pytest
from app.models.product import Product

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
