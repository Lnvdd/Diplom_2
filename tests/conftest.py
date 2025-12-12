import pytest
import allure
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.user_api import UserAPI
from api.order_api import OrderAPI
from data.user_data import UserData
from config import STATUS_CODES


@pytest.fixture
def user_api():
    api = UserAPI()
    yield api
    api.clear_tokens()


@pytest.fixture
def order_api():
    api = OrderAPI()
    yield api
    api.clear_tokens()


@pytest.fixture
def registered_user(user_api):
    """Фикстура создаёт пользователя как предусловие, БЕЗ проверок."""
    user_data = UserData.valid_user()
    with allure.step("Регистрируем пользователя для последующих тестов"):
        user_api.register_user(
            user_data["email"],
            user_data["password"],
            user_data["name"],
        )
    yield user_data
    user_api.clear_tokens()


@pytest.fixture
def order_api_with_auth(user_api, order_api, registered_user):
    """Фикстура подготавливает авторизованный order_api, БЕЗ assert-ов."""
    user_data = registered_user

    with allure.step("Авторизуемся для создания заказов"):
        user_api.login_user(
            user_data["email"],
            user_data["password"],
        )

    order_api.set_tokens(
        user_api.access_token,
        user_api.refresh_token,
    )

    yield order_api

    order_api.clear_tokens()
    user_api.clear_tokens()
