import requests
from config import BASE_URL

class BaseAPI:
    def __init__(self):
        self.session = requests.Session()
        self.access_token = None
        self.refresh_token = None
        self.user_data = {}

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{BASE_URL}{endpoint}"
        if self.access_token:
            self.session.headers.update({
                'Authorization': f'Bearer {self.access_token}'
            })
        try:
            response = self.session.request(method, url, **kwargs, timeout=10)
            return response
        except requests.exceptions.ConnectionError as e:
            return self._create_mock_response(503, {'success': False, 'message': 'Connection error'})
        except requests.exceptions.Timeout as e:
            return self._create_mock_response(504, {'success': False, 'message': 'Timeout error'})
        except requests.exceptions.RequestException as e:
            return self._create_mock_response(500, {'success': False, 'message': str(e)})

    def _create_mock_response(self, status_code, json_data):
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self._json = json_data

            def json(self):
                return self._json

        return MockResponse(status_code, json_data)

    def set_auth_headers(self, access_token, refresh_token=None):
        self.access_token = access_token
        if refresh_token:
            self.refresh_token = refresh_token

    def clear_tokens(self):
        self.access_token = None
        self.refresh_token = None
        self.user_data = {}