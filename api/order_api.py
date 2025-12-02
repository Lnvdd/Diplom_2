from api.base_api import BaseAPI
from config import ENDPOINTS, STATUS_CODES


class OrderAPI(BaseAPI):
    
    def create_order(self, ingredients):
        payload = {'ingredients': ingredients}
        response = self._make_request('POST', ENDPOINTS['create_order'], json=payload)
        return response
    
    def get_user_orders(self):
        response = self._make_request('GET', ENDPOINTS['user_orders'])
        return response
    
    def get_all_orders(self):
        response = self._make_request('GET', ENDPOINTS['get_orders'])
        return response
    
    def get_ingredients(self):
        response = self._make_request('GET', ENDPOINTS['get_ingredients'])
        return response
