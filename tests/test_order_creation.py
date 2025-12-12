import allure
import pytest

from config import STATUS_CODES
from data.order_data import OrderData


@allure.feature("Order Creation")
@allure.story("Burger Order Management")
class TestOrderCreation:

    @allure.title("Авторизованный пользователь может создать заказ")
    @allure.description("Проверка статуса ответа")
    @allure.severity("critical")
    def test_create_order_with_auth_success_status(self, order_api_with_auth):
        order_data = OrderData.order_with_multiple_ingredients()

        with allure.step("Создаем заказ с авторизацией"):
            response = order_api_with_auth.create_order(order_data["ingredients"])

        assert response.status_code == STATUS_CODES["ok"]

    @allure.title("Авторизованный пользователь получает success=True")
    @allure.description("Проверка флага успеха")
    @allure.severity("critical")
    def test_create_order_with_auth_success_flag(self, order_api_with_auth):
        order_data = OrderData.order_with_multiple_ingredients()

        with allure.step("Создаем заказ с авторизацией"):
            response = order_api_with_auth.create_order(order_data["ingredients"])

        assert response.json().get("success") is True

    @allure.title("Авторизованный заказ содержит номер")
    @allure.description("Проверка что номер заказа установлен")
    @allure.severity("critical")
    def test_create_order_with_auth_has_number(self, order_api_with_auth):
        order_data = OrderData.order_with_multiple_ingredients()

        with allure.step("Создаем заказ с авторизацией"):
            response = order_api_with_auth.create_order(order_data["ingredients"])

        order_number = response.json().get("order", {}).get("number")
        assert order_number is not None

    @allure.title("Неавторизованный пользователь может создать заказ")
    @allure.description("Проверка статуса ответа")
    @allure.severity("critical")
    def test_create_order_without_auth_success_status(self, order_api):
        order_data = OrderData.order_with_multiple_ingredients()

        with allure.step("Создаем заказ без авторизации"):
            response = order_api.create_order(order_data["ingredients"])

        assert response.status_code == STATUS_CODES["ok"]

    @allure.title("Неавторизованный пользователь получает success=True")
    @allure.description("Проверка флага успеха")
    @allure.severity("critical")
    def test_create_order_without_auth_success_flag(self, order_api):
        order_data = OrderData.order_with_multiple_ingredients()

        with allure.step("Создаем заказ без авторизации"):
            response = order_api.create_order(order_data["ingredients"])

        assert response.json().get("success") is True

    @allure.title("Неавторизованный заказ содержит номер")
    @allure.description("Проверка что номер заказа установлен")
    @allure.severity("critical")
    def test_create_order_without_auth_has_number(self, order_api):
        order_data = OrderData.order_with_multiple_ingredients()

        with allure.step("Создаем заказ без авторизации"):
            response = order_api.create_order(order_data["ingredients"])

        order_number = response.json().get("order", {}).get("number")
        assert order_number is not None

    @pytest.mark.parametrize("order_method,description", [
        (OrderData.order_with_one_ingredient, "одним ингредиентом"),
        (OrderData.order_with_multiple_ingredients, "несколькими ингредиентами"),
    ])
    @allure.title("Заказ успешно создается с разным количеством ингредиентов")
    @allure.description("Проверка статуса ответа")
    @allure.severity("high")
    def test_create_order_with_ingredients_status(self, order_api, order_method, description):
        order_data = order_method()

        with allure.step(f"Создаем заказ с {description}"):
            response = order_api.create_order(order_data["ingredients"])

        assert response.status_code == STATUS_CODES["ok"]

    @pytest.mark.parametrize("order_method,description", [
        (OrderData.order_with_one_ingredient, "одним ингредиентом"),
        (OrderData.order_with_multiple_ingredients, "несколькими ингредиентами"),
    ])
    @allure.title("Заказ содержит флаг успеха")
    @allure.description("Проверка success=True")
    @allure.severity("high")
    def test_create_order_with_ingredients_success_flag(self, order_api, order_method, description):
        order_data = order_method()

        with allure.step(f"Создаем заказ с {description}"):
            response = order_api.create_order(order_data["ingredients"])

        assert response.json().get("success") is True

    @pytest.mark.parametrize("order_method,description", [
        (OrderData.order_with_one_ingredient, "одним ингредиентом"),
        (OrderData.order_with_multiple_ingredients, "несколькими ингредиентами"),
    ])
    @allure.title("Заказ содержит номер")
    @allure.description("Проверка что номер установлен")
    @allure.severity("high")
    def test_create_order_with_ingredients_number(self, order_api, order_method, description):
        order_data = order_method()

        with allure.step(f"Создаем заказ с {description}"):
            response = order_api.create_order(order_data["ingredients"])

        order_number = response.json().get("order", {}).get("number")
        assert order_number is not None

    @pytest.mark.parametrize("invalid_method,description", [
        (OrderData.order_without_ingredients, "без ингредиентов"),
        (OrderData.order_with_invalid_ingredient, "с невалидным ингредиентом"),
        (OrderData.order_with_mixed_ingredients, "со смешанными ингредиентами"),
    ])
    @allure.title("Заказ не создается с неправильными ингредиентами")
    @allure.description("Проверка валидации ингредиентов")
    @allure.severity("high")
    def test_create_order_error(self, order_api, invalid_method, description):
        order_data = invalid_method()

        with allure.step(f"Пытаемся создать заказ {description}"):
            response = order_api.create_order(order_data["ingredients"])

        assert response.status_code != STATUS_CODES["ok"]
