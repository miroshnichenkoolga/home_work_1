
import pytest
from home_work3 import Product, Cart

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    def test_product_check_quantity(self, product):
        assert product.check_quantity(500) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        product.buy(200)
        assert product.quantity == 800

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError, match="Недостаточно товара на складе"):
            product.buy(2000)

class TestCart:
    def test_add_product(self, cart, product):
        cart.add_product(product, 2)
        assert cart.products[product] == 2

    def test_remove_product(self, cart, product):
        cart.add_product(product, 5)
        cart.remove_product(product, 3)
        assert cart.products[product] == 2

    def test_remove_product_entirely(self, cart, product):
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 5)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 2)
        assert cart.get_total_price() == 200

    def test_buy_success(self, cart, product):
        cart.add_product(product, 2)
        cart.buy()
        assert product.quantity == 998
        assert len(cart.products) == 0

    def test_buy_insufficient_stock(self, cart, product):
        cart.add_product(product, 2000)
        with pytest.raises(ValueError, match=f"Недостаточно товара {product.name} на складе"):
            cart.buy()
