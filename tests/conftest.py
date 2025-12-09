import pytest
import allure
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.user_api import UserAPI
from api.order_api import OrderAPI
from data.user_data import UserData
from config import STATUS_CODES

# ✅ ЧИСТАЯ фикстура - только инициализирует API
@pytest.fixture
def user_api():
    api = UserAPI()
    yield api
    api.clear_tokens()

# ✅ ЧИСТАЯ фикстура - только инициализирует API
@pytest.fixture
def order_api():
    api = OrderAPI()
    yield api
    api.clear_tokens()

# ✅ Фикстура создает авторизованный API БЕЗ прокидывания данных
@pytest.fixture
def order_api_with_auth(user_api, order_api):
    user_data = UserData.valid_user()
    
    with allure.step("Регистрируем пользователя для авторизации"):
        response = user_api.register_user(
            user_data["email"],
            user_data["password"],
            user_data["name"],
        )
        assert response.status_code == STATUS_CODES["ok"]
    
    order_api.set_tokens(
        user_api.access_token,
        user_api.refresh_token,
    )
    
    yield order_api
    
    order_api.clear_tokens()
    user_api.clear_tokens()