import json

import stripe

from api_stripe.models import Item
from project_api_stripe.settings import logger, STRIPE_SK


def create_product(name_product: str) -> str:
    """ Создание product_id """
    stripe.api_key = STRIPE_SK
    try:
        product = stripe.Product.create(name=name_product)
    except Exception as err:
        return f"failed to create product {err}"

    product = json.dumps(product)
    product_id = json.loads(product)['id']
    logger.info(f"product_id={product_id}")

    return product_id


def create_price(product: Item):
    """
    Создание price id
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
        mode="payment",
    )
    customer_json = json.dumps(customer)
    customer_id = json.loads(customer_json)['id']
    logger.debug(f"customer_id={customer_id}")

    return customer_id


def find_product(product_id: int) -> Item | None:
    try:
        product = Item.objects.get(id=product_id)
    except Exception as err:
        logger.debug(f"This product DoesNotExist {err}")

        return None

    return product