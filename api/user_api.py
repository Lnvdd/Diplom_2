import allure

from api.base_api import BaseAPI

from config import ENDPOINTS, STATUS_CODES

class UserAPI(BaseAPI):

    def register_user(self, email, password, name):
        """Регистрирует нового пользователя."""
        payload = {
            "email": email,
            "password": password,
            "name": name,
        }
        
        response = self._make_request("POST", ENDPOINTS["register_user"], json=payload)
        
        data = response.json()
        self.set_tokens(
            data.get("accessToken"),
            data.get("refreshToken"),
        )
        
        return response

    def login_user(self, email, password):
        """Авторизует пользователя."""
        payload = {
            "email": email,
            "password": password,
        }
        
        response = self._make_request("POST", ENDPOINTS["login_user"], json=payload)
        
        data = response.json()
        self.set_tokens(
            data.get("accessToken"),
            data.get("refreshToken"),
        )
        
        return response

    def delete_user(self, access_token):
        """Удаляет пользователя."""
        headers = {"Authorization": access_token}
        return self._make_request("DELETE", ENDPOINTS["delete_user"], headers=headers)

    def update_user_email(self, email):
        """Обновляет email пользователя."""
        payload = {"email": email}
        return self._make_request("PATCH", ENDPOINTS["update_user"], json=payload)

    def update_user_name(self, name):
        """Обновляет имя пользователя."""
        payload = {"name": name}
        return self._make_request("PATCH", ENDPOINTS["update_user"], json=payload)

    def update_user_password(self, password):
        """Обновляет пароль пользователя."""
        payload = {"password": password}
        return self._make_request("PATCH", ENDPOINTS["update_user"], json=payload)

    def update_user_email_and_name(self, email, name):
        """Обновляет email и имя пользователя."""
        payload = {"email": email, "name": name}
        return self._make_request("PATCH", ENDPOINTS["update_user"], json=payload)

    def update_user_email_and_password(self, email, password):
        """Обновляет email и пароль пользователя."""
        payload = {"email": email, "password": password}
        return self._make_request("PATCH", ENDPOINTS["update_user"], json=payload)

    def update_user_name_and_password(self, name, password):
        """Обновляет имя и пароль пользователя."""
        payload = {"name": name, "password": password}
        return self._make_request("PATCH", ENDPOINTS["update_user"], json=payload)

    def update_user_all(self, email, name, password):
        """Обновляет все данные пользователя."""
        payload = {"email": email, "name": name, "password": password}
        return self._make_request("PATCH", ENDPOINTS["update_user"], json=payload)