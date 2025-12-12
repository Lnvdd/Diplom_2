import allure
import pytest

from config import STATUS_CODES
from data.user_data import UserData


@allure.feature("User Creation")
@allure.story("User Registration")
class TestUserCreation:

    # test_create_user_success - разбит на 3 атомарных теста
    @allure.title("Пользователя можно создать с валидными данными")
    @allure.description("Проверка статуса ответа при регистрации")
    @allure.severity("critical")
    def test_create_user_success_status(self, user_api):
        user_data = UserData.valid_user()

        with allure.step("Отправляем запрос на создание пользователя"):
            response = user_api.register_user(
                user_data["email"],
                user_data["password"],
                user_data["name"],
            )

        assert response.status_code == STATUS_CODES["ok"]

    @allure.title("При регистрации возвращается флаг success=True")
    @allure.description("Проверка флага успеха в ответе")
    @allure.severity("critical")
    def test_create_user_success_flag(self, user_api):
        user_data = UserData.valid_user()

        with allure.step("Отправляем запрос на создание пользователя"):
            response = user_api.register_user(
                user_data["email"],
                user_data["password"],
                user_data["name"],
            )

        assert response.json().get("success") is True

    @allure.title("При регистрации возвращается токен доступа")
    @allure.description("Проверка что токен установлен")
    @allure.severity("critical")
    def test_create_user_success_token(self, user_api):
        user_data = UserData.valid_user()

        with allure.step("Отправляем запрос на создание пользователя"):
            response = user_api.register_user(
                user_data["email"],
                user_data["password"],
                user_data["name"],
            )

        assert response.json().get("accessToken") is not None

    # test_create_duplicate_user - разбит на 2 части
    @allure.title("Попытка создать пользователя с существующим email")
    @allure.description("Проверка что дубликат не создается")
    @allure.severity("critical")
    def test_create_duplicate_user_error_status(self, user_api):
        user_data = UserData.valid_user()

        with allure.step("Создаем первого пользователя"):
            user_api.register_user(
                user_data["email"],
                user_data["password"],
                user_data["name"],
            )

        with allure.step("Пытаемся создать пользователя с тем же email"):
            response2 = user_api.register_user(
                user_data["email"],
                "DifferentPassword123!",
                "Different Name",
            )

        assert response2.status_code != STATUS_CODES["ok"]

    # test_create_user_missing_fields - разбит на отдельные тесты для каждого поля
    @allure.title("Нельзя создать пользователя без email")
    @allure.description("Проверка валидации обязательного поля email")
    @allure.severity("critical")
    def test_create_user_missing_email(self, user_api):
        user_data = UserData.invalid_user_missing_email()

        with allure.step("Отправляем запрос без email"):
            response = user_api.register_user(
                user_data.get("email", ""),
                user_data.get("password", ""),
                user_data.get("name", ""),
            )

        assert response.status_code != STATUS_CODES["ok"]

    @allure.title("Нельзя создать пользователя без пароля")
    @allure.description("Проверка валидации обязательного поля password")
    @allure.severity("critical")
    def test_create_user_missing_password(self, user_api):
        user_data = UserData.invalid_user_missing_password()

        with allure.step("Отправляем запрос без пароля"):
            response = user_api.register_user(
                user_data.get("email", ""),
                user_data.get("password", ""),
                user_data.get("name", ""),
            )

        assert response.status_code != STATUS_CODES["ok"]

    @allure.title("Нельзя создать пользователя без имени")
    @allure.description("Проверка валидации обязательного поля name")
    @allure.severity("critical")
    def test_create_user_missing_name(self, user_api):
        user_data = UserData.invalid_user_missing_name()

        with allure.step("Отправляем запрос без имени"):
            response = user_api.register_user(
                user_data.get("email", ""),
                user_data.get("password", ""),
                user_data.get("name", ""),
            )

        assert response.status_code != STATUS_CODES["ok"]
