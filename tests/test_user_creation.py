import allure
import pytest
from config import STATUS_CODES
from data.user_data import UserData

@allure.feature("User Creation")
@allure.story("User Registration")
class TestUserCreation:

    @allure.title("Пользователя можно создать с валидными данными")
    @allure.description("Проверка успешной регистрации пользователя")
    @allure.severity("critical")
    def test_create_user_success(self, user_api):
        user_data = UserData.valid_user()
        
        with allure.step("Отправляем запрос на создание пользователя"):
            response = user_api.register_user(
                user_data["email"],
                user_data["password"],
                user_data["name"],
            )
        
        with allure.step("Проверяем статус ответа"):
            assert response.status_code == STATUS_CODES["ok"]
        
        with allure.step("Проверяем успешность"):
            assert response.json().get("success") is True
        
        with allure.step("Проверяем что токен установлен"):
            assert response.json().get("accessToken") is not None

    @allure.title("Нельзя создать пользователя с существующим email")
    @allure.description("Проверка что нельзя создать дубликат пользователя")
    @allure.severity("critical")
    def test_create_duplicate_user(self, user_api):
        user_data = UserData.valid_user()
        
        with allure.step("Создаем первого пользователя"):
            response1 = user_api.register_user(
                user_data["email"],
                user_data["password"],
                user_data["name"],
            )
            assert response1.status_code == STATUS_CODES["ok"]
        
        with allure.step("Пытаемся создать пользователя с тем же email"):
            response2 = user_api.register_user(
                user_data["email"],
                "DifferentPassword123!",
                "Different Name",
            )
        
        with allure.step("Проверяем что регистрация не прошла"):
            assert response2.status_code != STATUS_CODES["ok"]

    @pytest.mark.parametrize("missing_field,user_method,description", [
        ("email", UserData.invalid_user_missing_email, "без email"),
        ("password", UserData.invalid_user_missing_password, "без пароля"),
        ("name", UserData.invalid_user_missing_name, "без имени"),
    ])
    @allure.title("Нельзя создать пользователя с пустыми обязательными полями")
    @allure.description("Проверка валидации обязательных полей")
    @allure.severity("critical")
    def test_create_user_missing_fields(self, user_api, missing_field, user_method, description):
        
        user_data = user_method()
        
        with allure.step(f"Отправляем запрос {description}"):
            response = user_api.register_user(
                user_data.get("email", ""),
                user_data.get("password", ""),
                user_data.get("name", ""),
            )
        
        with allure.step("Проверяем ошибку"):
            assert response.status_code != STATUS_CODES["ok"]
