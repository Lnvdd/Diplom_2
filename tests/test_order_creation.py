import allure
import pytest
from config import STATUS_CODES
from data.order_data import OrderData

@allure.feature("Order Creation")
@allure.story("Burger Order Management")
class TestOrderCreation:

    @allure.title("Авторизованный пользователь может создать заказ")
    @allure.description("Проверка успешного создания заказа с авторизацией")
    @allure.severity("critical")
    def test_create_order_with_auth_success(self, order_api_with_auth):
        order_data = OrderData.order_with_multiple_ingredients()
        
        with allure.step("Создаем заказ с авторизацией"):
            response = order_api_with_auth.create_order(order_data["ingredients"])
        
        with allure.step("Проверяем статус ответа"):
            assert response.status_code == STATUS_CODES["ok"]
        
        with allure.step("Проверяем успешность"):
            assert response.json().get("success") is True
        
        with allure.step("Проверяем что номер заказа установлен"):
            order_number = response.json().get("order", {}).get("number")
            # ✅ БЕЗ условия - прямой assert
            assert order_number is not None

    @allure.title("Неавторизованный пользователь может создать заказ")
    @allure.description("Проверка что заказ можно создать без авторизации")
    @allure.severity("critical")
    def test_create_order_without_auth_success(self, order_api):
        order_data = OrderData.order_with_multiple_ingredients()
        
        with allure.step("Создаем заказ без авторизации"):
            response = order_api.create_order(order_data["ingredients"])
        
        with allure.step("Проверяем статус ответа"):
            assert response.status_code == STATUS_CODES["ok"]
        
        with allure.step("Проверяем успешность"):
            assert response.json().get("success") is True
        
        with allure.step("Проверяем что номер заказа установлен"):
            order_number = response.json().get("order", {}).get("number")
            # ✅ БЕЗ условия - прямой assert
            assert order_number is not None

    @pytest.mark.parametrize("order_method,description", [
        (OrderData.order_with_one_ingredient, "одним ингредиентом"),
        (OrderData.order_with_multiple_ingredients, "несколькими ингредиентами"),
    ])
    @allure.title("Можно создать заказ с разным количеством ингредиентов")
    @allure.description("Проверка создания заказа с минимальным и максимальным составом")
    @allure.severity("high")
    def test_create_order_success(self, order_api, order_method, description):
        order_data = order_method()
        
        with allure.step(f"Создаем заказ с {description}"):
            response = order_api.create_order(order_data["ingredients"])
        
        with allure.step("Проверяем успешность"):
            assert response.status_code == STATUS_CODES["ok"]
            assert response.json().get("success") is True
        
        with allure.step("Проверяем что номер заказа установлен"):
            order_number = response.json().get("order", {}).get("number")
            # ✅ БЕЗ условия - прямой assert
            assert order_number is not None

    @pytest.mark.parametrize("invalid_method,description", [
        (OrderData.order_without_ingredients, "без ингредиентов"),
        (OrderData.order_with_invalid_ingredient, "с невалидным ингредиентом"),
        (OrderData.order_with_mixed_ingredients, "со смешанными ингредиентами"),
    ])
    @allure.title("Нельзя создать заказ с неправильными ингредиентами")
    @allure.description("Проверка валидации ингредиентов при создании заказа")
    @allure.severity("high")
    def test_create_order_error(self, order_api, invalid_method, description):
        order_data = invalid_method()
        
        with allure.step(f"Пытаемся создать заказ {description}"):
            response = order_api.create_order(order_data["ingredients"])
        
        with allure.step("Проверяем что статус не успешен"):
            assert response.status_code != STATUS_CODES["ok"]