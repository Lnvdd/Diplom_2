import allure
import pytest
from config import STATUS_CODES
from data.user_data import UserData

@allure.feature("User Login")
@allure.story("User Authentication")
class TestUserLogin:

    @allure.title("Пользователь может авторизоваться с валидными данными")
    @allure.description("Проверка успешной авторизации")
    @allure.severity("critical")
    def test_login_user_success(self, user_api):
        user_data = UserData.valid_user()
        
        with allure.step("Создаем пользователя"):
            register_response = user_api.register_user(
                user_data["email"],
                user_data["password"],
                user_data["name"],
            )
            assert register_response.status_code == STATUS_CODES["ok"]
        
        user_api.clear_tokens()
        
        with allure.step("Авторизуемся"):
            login_response = user_api.login_user(
                user_data["email"],
                user_data["password"],
            )
        
        with allure.step("Проверяем что токен установлен"):
          
            assert login_response.status_code == STATUS_CODES["ok"]
            assert user_api.access_token is not None

    @pytest.mark.parametrize("invalid_data,description", [
        (UserData.invalid_login_wrong_email(), "неправильный email"),
        (UserData.invalid_login_empty_email(), "пустой email"),
        (UserData.invalid_login_empty_password(), "пустой пароль"),
    ])
    @allure.title("Авторизация не проходит с неправильными данными")
    @allure.description("Проверка что неправильные данные приводят к ошибке")
    @allure.severity("critical")
    def test_login_user_invalid(self, user_api, invalid_data, description):
        with allure.step(f"Пытаемся авторизоваться с {description}"):
            response = user_api.login_user(
                invalid_data["email"],
                invalid_data["password"],
            )
        
        with allure.step("Проверяем ошибку"):
            assert response.status_code != STATUS_CODES["ok"]