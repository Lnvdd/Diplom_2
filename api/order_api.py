import requests

from api.base_api import BaseAPI

from config import ENDPOINTS

class OrderAPI(BaseAPI):

    def create_order(self, ingredients: list) -> requests.Response:
        """Создает заказ."""
        payload = {"ingredients": ingredients}
        return self._make_request("POST", ENDPOINTS["create_order"], json=payload)

    def delete_order(self, order_id: str) -> requests.Response:
        """Удаляет заказ по ID."""
        endpoint = ENDPOINTS["delete_order"].format(id=order_id)
        return self._make_request("DELETE", endpoint)

    def get_orders(self) -> requests.Response:
        """Получает список заказов текущего пользователя."""
        return self._make_request("GET", ENDPOINTS["get_orders"])

    def get_ingredients(self) -> requests.Response:
        """Получает все доступные ингредиенты."""
        return self._make_request("GET", ENDPOINTS["get_ingredients"])