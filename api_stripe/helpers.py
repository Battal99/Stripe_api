import json

import stripe

# class ApiStripe:
#     def __init__(self, spi_key):
#         self.product = None
#         self.price = None
#         stripe.api_key = spi_key
#
from api_stripe.models import Item


def create_product(name_product: str) -> str:
    """ """
    stripe.api_key = "sk_test_51M4rA9Gjg9ZFyR2ke94VEq5LCT57rK7lr5TieJ4ygUwE6uy7i0R5Tm2hzmcDU56X1jxphbeqkQ6CbnXD41MC3kcG00czK20yyG"
    try:
        product = stripe.Product.create(name=name_product)
    except Exception as err:
        return f"failed to create product {err}"

    product = json.dumps(product)
    product_id = json.loads(product)['id']
    print(product_id)
    return product_id


def create_price(product: Item):
    """

    :return:
    """
    product_id = create_product(product.name)
    price_create = json.dumps(stripe.Price.create(
        unit_amount=product.price,
        currency="usd",
        product=product_id,
    ))
    price_id = json.loads(price_create)['id']
    return price_id


def create_session(product: Item) -> str:
    price_id = create_price(product)
    customer = stripe.checkout.Session.create(
        success_url="http://127.0.0.1/success",
        cancel_url="http://127.0.0.1/cancel",
        line_items=[
            {"price": price_id,
             "quantity": 1,
             },
        ],
        metadata={
            "product_id": create_product(product.name)
        },
        mode="payment", )
    customer_json = json.dumps(customer)
    customer_id = json.loads(customer_json)['id']
    # customer_url = json.loads(customer_json)['url']
    print(customer_id)

    return customer_id


def find_product(product_id: int) -> Item | None:
    try:
        product = Item.objects.get(id=product_id)
    except Exception as err:
        print(f"This product DoesNotExist {err}")

        return None

    return product
