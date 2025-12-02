import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/..'))


@pytest.fixture
def user_api():
    from api.user_api import UserAPI
    return UserAPI()


@pytest.fixture
def registered_user(user_api):
    from data.user_data import UserData
    user_data = UserData.valid_user()
    response = user_api.register_user(
        user_data['email'],
        user_data['password'],
        user_data['name']
    )
    return user_api, user_data, response


@pytest.fixture
def logged_in_user(user_api):
    from data.user_data import UserData
    user_data = UserData.valid_user()

    user_api.register_user(
        user_data['email'],
        user_data['password'],
        user_data['name']
    )
    response = user_api.login_user(user_data['email'], user_data['password'])
    return user_api, user_data, response


@pytest.fixture
def order_api():
    from api.order_api import OrderAPI
    return OrderAPI()


@pytest.fixture
def order_api_with_auth(logged_in_user):
    from api.order_api import OrderAPI
    user_api, user_data, _ = logged_in_user
    
    
    order_api = OrderAPI()
    order_api.set_auth_headers(user_api.access_token, user_api.refresh_token)
    
    return order_api


@pytest.fixture
def valid_user_data():
    """Валидные данные пользователя"""
    from data.user_data import UserData
    return UserData.valid_user()


@pytest.fixture
def valid_order_data():
    from data.order_data import OrderData
    return OrderData.order_with_multiple_ingredients()


@pytest.fixture
def all_valid_ingredients():
    from data.order_data import OrderData
    return OrderData.VALID_INGREDIENTS


@pytest.fixture
def invalid_ingredient():
    from data.order_data import OrderData
    return OrderData.INVALID_INGREDIENT