from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from api_stripe.api_utils import stripe_api_key
import stripe
import json
from django.views.generic import TemplateView
from api_stripe.helpers import create_session, find_product

# Create your views here.
from api_stripe.models import Item


def get_buy_id(request, item_id: int):
    """ """
    product: Item = find_product(item_id)
    if product is None:
        return HttpResponse(f"This product DoesNotExist")

    # session_id: str = create_session(product)
    session_id: str = create_session(product)
    print(type(product))

    # result = json.dumps({"session_id": session_id})
    return JsonResponse({'sessionId': session_id})
    # return redirect(session_id, code=303)


def get_payment(request, item_id: int):
    product: Item = find_product(item_id)
    if product is None:
        return HttpResponse(f"This product DoesNotExist")

    # session: str = create_session(product)

    # return redirect(session.url, code=303)
    return render(request, "payment.html", {"product": product})


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
