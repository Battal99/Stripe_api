from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from api_stripe.helpers import create_session, find_product
from api_stripe.models import Item
from project_api_stripe.settings import logger, STRIPE_PUBLIC_KEY


def get_buy_id_view(request, item_id: int):
    """ Запрос  GET: получение  Stripe
        Session Id для оплаты выбранного Item
        :return Json
    """
    product: Item = find_product(item_id)
    if product is None:
        logger.debug("This product does not exist")
        return HttpResponse(f"This product does not exist", status=404)

    session_id = create_session(product)['id']
    logger.info(product)

    return JsonResponse({'sessionId': session_id})


def get_payment_view(request, item_id: int):
    """ Запрос  GET на которой будет информация
       о выбранном Item и кнопка Buy.
    """
    product: Item = find_product(item_id)
    if product is None:
        logger.debug("This product does not exist")
        return HttpResponse(f"This product DoesNotExist", status=404)

    return render(request, "payment.html", {
        "product": product,
        "STRIPE_PUBLIC_KEY": STRIPE_PUBLIC_KEY})


class SuccessView(TemplateView):
    template_name = "success.html"


class CanceledView(TemplateView):
    template_name = "cancel.html"
