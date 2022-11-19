import pytest
import requests


class TestApiStripe:

    @pytest.mark.parametrize("buy_id", [i for i in range(1, 4)])
    def test_get_buy_id_view(self, buy_id):
        response = requests.get(f"http://127.0.0.1:8000/buy/{buy_id}")

        assert response.status_code == 200
        assert response.text

    def test_invalid_get_buy_id_view(self):
        response = requests.get("http://127.0.0.1:8000/buy/25")

        assert response.status_code == 404
        assert response.text == 'This product does not exist'

    @pytest.mark.parametrize("item", [i for i in range(1, 4)])
    def test_get_payment_view(self, item):
        response = requests.get(f"http://127.0.0.1:8000/buy/{item}")

        assert response.status_code == 200
        assert response.text

    def test_invalid_get_payment_view(self):
        response = requests.get("http://127.0.0.1:8000/buy/423")

        assert response.status_code == 404
        assert response.text == 'This product does not exist'
