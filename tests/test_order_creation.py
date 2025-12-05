import allure
import pytest

from config import STATUS_CODES


@allure.feature('Order Creation')
@allure.story('Burger Order Management')
class TestOrderCreation:

    @allure.title('Авторизованный пользователь может создать заказ')
    @allure.description('Проверка успешного создания заказа с авторизацией')
    @allure.severity('critical')
    def test_create_order_with_auth_success(self, order_api_with_auth):
        from data.order_data import OrderData
        order_data = OrderData.order_with_multiple_ingredients()

        with allure.step('Создаем заказ с авторизацией'):
            response = order_api_with_auth.create_order(order_data['ingredients'])

        with allure.step('Проверяем статус ответа'):
            assert response.status_code == STATUS_CODES['ok']

        with allure.step('Проверяем успешность'):
            assert response.json().get('success') is True

        with allure.step('Проверяем что номер заказа установлен'):
            assert response.json().get('order', {}).get('number') is not None

    @allure.title('Неавторизованный пользователь может создать заказ')
    @allure.description('Проверка что заказ можно создать без авторизации')
    @allure.severity('critical')
    def test_create_order_without_auth_success(self, order_api):
        from data.order_data import OrderData
        order_data = OrderData.order_with_multiple_ingredients()

        with allure.step('Создаем заказ без авторизации'):
            response = order_api.create_order(order_data['ingredients'])

        with allure.step('Проверяем статус ответа'):
            assert response.status_code == STATUS_CODES['ok']

        with allure.step('Проверяем успешность'):
            assert response.json().get('success') is True

    @allure.title('Можно создать заказ с одним ингредиентом')
    @allure.description('Проверка создания заказа с минимальным составом')
    @allure.severity('high')
    def test_create_order_with_one_ingredient(self, order_api):
        from data.order_data import OrderData
        order_data = OrderData.order_with_one_ingredient()

        with allure.step('Создаем заказ с одним ингредиентом'):
            response = order_api.create_order(order_data['ingredients'])

        with allure.step('Проверяем успешность'):
            assert response.status_code == STATUS_CODES['ok']
            assert response.json().get('success') is True

    @allure.title('Нельзя создать заказ без ингредиентов - ошибка')
    @allure.description('Проверка валидации - заказ должен иметь ингредиенты')
    @allure.severity('critical')
    def test_create_order_without_ingredients_error(self, order_api):
        from data.order_data import OrderData
        order_data = OrderData.order_without_ingredients()

        with allure.step('Пытаемся создать заказ без ингредиентов'):
            response = order_api.create_order(order_data['ingredients'])

        with allure.step('Проверяем что статус не успешен'):
           
            assert response.status_code != STATUS_CODES['ok']

    @allure.title('Нельзя создать заказ с невалидным ингредиентом - ошибка')
    @allure.description('Проверка что невалидный хеш ингредиента приводит к ошибке')
    @allure.severity('high')
    def test_create_order_with_invalid_ingredient_error(self, order_api):
        from data.order_data import OrderData
        order_data = OrderData.order_with_invalid_ingredient()

        with allure.step('Пытаемся создать заказ с невалидным ингредиентом'):
            response = order_api.create_order(order_data['ingredients'])

        with allure.step('Проверяем что статус не успешен'):
        
            assert response.status_code != STATUS_CODES['ok']

    @allure.title('Нельзя создать заказ с смешанными ингредиентами - ошибка')
    @allure.description('Проверка что один невалидный ингредиент портит весь заказ')
    @allure.severity('high')
    def test_create_order_with_mixed_ingredients_error(self, order_api):
        from data.order_data import OrderData
        order_data = OrderData.order_with_mixed_ingredients()

        with allure.step('Пытаемся создать заказ с смешанными ингредиентами'):
            response = order_api.create_order(order_data['ingredients'])

        with allure.step('Проверяем что статус не успешен'):
           
            assert response.status_code != STATUS_CODES['ok']