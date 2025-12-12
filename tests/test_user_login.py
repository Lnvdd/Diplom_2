import allure
import pytest

from config import STATUS_CODES
from data.user_data import UserData


@allure.feature("User Login")
@allure.story("User Authentication")
class TestUserLogin:

    @allure.title("Пользователь может авторизоваться с валидными данными")
    @allure.description("Проверка статуса ответа при авторизации")
    @allure.severity("critical")
    def test_login_user_success_status(self, user_api, registered_user):
        user_data = registered_user

        with allure.step("Авторизуемся"):
            login_response = user_api.login_user(
                user_data["email"],
                user_data["password"],
            )

        assert login_response.status_code == STATUS_CODES["ok"]

    @allure.title("При авторизации устанавливается токен")
    @allure.description("Проверка что токен получен")
    @allure.severity("critical")
    def test_login_user_success_token(self, user_api, registered_user):
        user_data = registered_user

        with allure.step("Авторизуемся"):
            user_api.login_user(
                user_data["email"],
                user_data["password"],
            )

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

        assert response.status_code != STATUS_CODES["ok"]
