import allure
import pytest

from config import STATUS_CODES


@allure.feature('User Login')
@allure.story('User Authentication')
class TestUserLogin:

    @allure.title('Пользователь может авторизоваться с валидными данными')
    @allure.description('Проверка успешной авторизации')
    @allure.severity('critical')
    def test_login_user_success(self, logged_in_user):
        user_api, email, password, name = logged_in_user
        
        
        response = user_api.login_user(email, password)

        with allure.step('Проверяем статус ответа'):
            assert response.status_code == STATUS_CODES['ok']

        with allure.step('Проверяем успешность'):
            assert response.json().get('success') is True

        with allure.step('Проверяем токен'):
            assert response.json().get('accessToken') is not None

        with allure.step('Проверяем что пользователь авторизован'):
            assert user_api.access_token is not None

    @allure.title('Нельзя авторизоваться с неправильным email')
    @allure.description('Проверка что неправильный email приводит к ошибке')
    @allure.severity('critical')
    def test_login_user_invalid_email(self, user_api):
        from data.user_data import UserData
        invalid_login = UserData.invalid_login_wrong_email()

        with allure.step('Пытаемся авторизоваться с неправильным email'):
            response = user_api.login_user(
                invalid_login['email'],
                invalid_login['password']
            )

        with allure.step('Проверяем ошибку'):
            
            assert response.status_code != STATUS_CODES['ok']

    @allure.title('Нельзя авторизоваться с пустым email')
    @allure.description('Проверка валидации пустого email')
    @allure.severity('critical')
    def test_login_user_empty_email(self, user_api):
        from data.user_data import UserData
        invalid_login = UserData.invalid_login_empty_email()

        with allure.step('Пытаемся авторизоваться с пустым email'):
            response = user_api.login_user(
                invalid_login['email'],
                invalid_login['password']
            )

        with allure.step('Проверяем ошибку'):
            
            assert response.status_code != STATUS_CODES['ok']

    @allure.title('Нельзя авторизоваться с пустым паролем')
    @allure.description('Проверка валидации пустого пароля')
    @allure.severity('critical')
    def test_login_user_empty_password(self, user_api):
        from data.user_data import UserData
        invalid_login = UserData.invalid_login_empty_password()

        with allure.step('Пытаемся авторизоваться с пустым паролем'):
            response = user_api.login_user(
                invalid_login['email'],
                invalid_login['password']
            )

        with allure.step('Проверяем ошибку'):
            
            assert response.status_code != STATUS_CODES['ok']