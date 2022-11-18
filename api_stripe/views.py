from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from api_stripe.helpers import create_session, find_product
# Create your views here.
from api_stripe.models import Item
from project_api_stripe.settings import logger


def get_buy_id(request, item_id: int):
    """ Запрос  GET: получение  Stripe
        Session Id для оплаты выбранного Item
        :return Json
    """
    product: Item = find_product(item_id)
    if product is None:
        logger.debug("This product does not exist")
        return HttpResponse(f"This product does not exist")

    session_id: str = create_session(product)
    logger.info(product)

    return JsonResponse({'sessionId': session_id})


def get_payment(request, item_id: int):
    """ Запрос  GET на которой будет информация
       о выбранном Item и кнопка Buy.
    """
    product: Item = find_product(item_id)
    if product is None:
        logger.debug("This product does not exist")
        return HttpResponse(f"This product DoesNotExist")

    return render(request, "payment.html", {"product": product})
