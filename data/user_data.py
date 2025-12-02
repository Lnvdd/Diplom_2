from datetime import datetime
from utils.helpers import generate_unique_email, generate_random_password, generate_random_name


class UserData:
    
    @staticmethod
    def valid_user():
        return {
            'email': generate_unique_email(),
            'password': 'Test1234!@',
            'name': generate_random_name()
        }
    
    @staticmethod
    def valid_user_with_custom_email(email):
        return {
            'email': email,
            'password': 'Test1234!@',
            'name': generate_random_name()
        }
    
    @staticmethod
    def invalid_user_missing_email():
        return {
            'password': 'Test1234!@',
            'name': generate_random_name()
        }
    
    @staticmethod
    def invalid_user_missing_password():
        return {
            'email': generate_unique_email(),
            'name': generate_random_name()
        }
    
    @staticmethod
    def invalid_user_missing_name():
        return {
            'email': generate_unique_email(),
            'password': 'Test1234!@'
        }
    
    @staticmethod
    def invalid_login_empty_email():
        return {
            'email': '',
            'password': 'Test1234!@'
        }
    
    @staticmethod
    def invalid_login_empty_password():
        return {
            'email': generate_unique_email(),
            'password': ''
        }
    
    @staticmethod
    def invalid_login_both_empty():
        return {
            'email': '',
            'password': ''
        }
    
    @staticmethod
    def invalid_login_wrong_email():
        return {
            'email': 'nonexistent@example.com',
            'password': 'WrongPassword123!'
        }
