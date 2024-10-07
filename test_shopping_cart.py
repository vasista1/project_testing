from shopping_cart import ShoppingCart
from pytest import raises, fixture

@fixture
def cart():
    return ShoppingCart(6)

def test_add_to_cart(cart):
    res = cart.add('apple')
    assert 'apple' == res

def test_add_multiple_items_to_cart(cart):
    cart.add('mango')
    res = cart.add(['apple','orange','grapes'])
    assert res == ['apple','orange','grapes']

def test_price_of_cart(cart):
    res = cart.add(['apple','orange','grapes'])
    price_map={'apple':15, 'orange':20,'grapes':25, 'mango':30}
    res = cart.total_price(price_map)
    assert 60 == res

def test_max_limit(cart):
    for _ in range(6):
        cart.add('apple')
    with raises(OverflowError):
        cart.add('apple')

def test_raise_of_max_limit_with_multiple_items(cart):
    for _ in range(5):
        cart.add('apple')
    with raises(OverflowError):
        cart.add(['apple','orange','grapes'])
