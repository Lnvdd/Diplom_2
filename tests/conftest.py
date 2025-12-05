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
    yield user_api, user_data['email'], user_data['password'], user_data['name']
    _cleanup_user(user_api, user_data['email'])

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
    yield user_api, user_data['email'], user_data['password'], user_data['name']
    _cleanup_user(user_api, user_data['email'])

@pytest.fixture
def order_api():
    from api.order_api import OrderAPI
    return OrderAPI()

@pytest.fixture
def order_api_with_auth(logged_in_user):
    from api.order_api import OrderAPI
    user_api, email, password, name = logged_in_user
    order_api = OrderAPI()
    order_api.set_auth_headers(user_api.access_token, user_api.refresh_token)
    yield order_api
    order_api.clear_tokens()

@pytest.fixture
def valid_user_data():
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

def _cleanup_user(user_api, email):
    try:
        if hasattr(user_api, 'delete_user'):
            user_api.delete_user(email)
    except Exception as e:
        print(f"Не удалось удалить пользователя {email}: {e}")

def _cleanup_order(order_api, order_id):
    try:
        if hasattr(order_api, 'delete_order'):
            order_api.delete_order(order_id)
    except Exception as e:
        print(f"Не удалось удалить заказ {order_id}: {e}")

@pytest.fixture(autouse=True)
def cleanup_database():
    yield
    pass