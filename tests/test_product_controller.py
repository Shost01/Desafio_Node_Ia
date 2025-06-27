import pytest
from app.controllers.product_controller import ProductController

def test_controller_has_repository():
    controller = ProductController()
    assert hasattr(controller, 'repository')
