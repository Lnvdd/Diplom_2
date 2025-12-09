import requests

from config import BASE_URL

class BaseAPI:

    def __init__(self):
        self.session = requests.Session()
        self.access_token = None
        self.refresh_token = None

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Выполняет HTTP запрос."""
        url = f"{BASE_URL}{endpoint}"
        headers = kwargs.pop("headers", {})
        
        if self.access_token:
            headers["Authorization"] = self.access_token
        
        try:
            response = self.session.request(
                method,
                url,
                headers=headers,
                **kwargs,
                timeout=10
            )
            return response
        
        except requests.exceptions.Timeout as e:
            raise requests.exceptions.Timeout(
                f"Timeout при запросе {method} {url}: {str(e)}"
            )
        
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError(
                f"Ошибка соединения с {url}: {str(e)}"
            )
        
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(
                f"Ошибка запроса {method} {url}: {str(e)}"
            )

    def set_tokens(self, access_token: str, refresh_token: str):
        """Устанавливает токены."""
        self.access_token = access_token
        self.refresh_token = refresh_token

    def clear_tokens(self):
        """Очищает токены."""
        self.access_token = None
        self.refresh_token = None

    def close(self):
        """Закрывает сессию."""
        self.session.close()