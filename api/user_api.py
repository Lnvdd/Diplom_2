from api.base_api import BaseAPI
from config import ENDPOINTS, STATUS_CODES


class UserAPI(BaseAPI):
    
    def register_user(self, email, password, name):
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        
        response = self._make_request('POST', ENDPOINTS['register'], json=payload)
        
        if response and response.status_code == STATUS_CODES['ok']:
            data = response.json()
            if data.get('success'):
                self.access_token = data.get('accessToken', '').replace('Bearer ', '')
                self.refresh_token = data.get('refreshToken')
                self.user_data = data.get('user', {})
        return response
    
    def login_user(self, email, password):
        payload = {
            'email': email,
            'password': password
        }
        
        response = self._make_request('POST', ENDPOINTS['login'], json=payload)
        
        if response and response.status_code == STATUS_CODES['ok']:
            data = response.json()
            if data.get('success'):
                self.access_token = data.get('accessToken', '').replace('Bearer ', '')
                self.refresh_token = data.get('refreshToken')
                self.user_data = data.get('user', {})
        return response
    
    def logout_user(self):
        if not self.refresh_token:
            return None
        
        payload = {'token': self.refresh_token}
        response = self._make_request('POST', ENDPOINTS['logout'], json=payload)
        
        if response and response.status_code == STATUS_CODES['ok']:
            self.clear_tokens()
        return response
    
    def get_user(self):
        response = self._make_request('GET', ENDPOINTS['user'])
        return response
    
    def update_user(self, email=None, name=None, password=None):
        payload = {}
        
        if email:
            payload['email'] = email
        if name:
            payload['name'] = name
        if password:
            payload['password'] = password
        
        response = self._make_request('PATCH', ENDPOINTS['user'], json=payload)
        
        if response and response.status_code == STATUS_CODES['ok']:
            data = response.json()
            if data.get('success'):
                self.user_data = data.get('user', {})
        return response
    
    def delete_user(self):
        response = self._make_request('DELETE', ENDPOINTS['user'])
        
        if response and response.status_code == STATUS_CODES['ok']:
            self.clear_tokens()
        return response
