import pytest
from app.repositories.product_repository import ProductRepository
from app.models.product import Product

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
