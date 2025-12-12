import random
import string
from datetime import datetime


def generate_unique_email():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"testuser_{timestamp}_{random_suffix}@yandex.ru"


def generate_random_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return password + '!@'


def generate_random_name():
    names = ['Alex', 'John', 'Maria', 'Ivan', 'Anna', 'Peter', 'Elena', 'Boris']
    return random.choice(names)


def extract_order_number(response_json):
    if response_json and response_json.get('order'):
        return response_json['order'].get('number')
    return None


def is_valid_token(token):
    return token is not None and len(token) > 0


def compare_user_data(user1, user2):
    return user1.get('email') == user2.get('email') and user1.get('name') == user2.get('name')


def get_error_message(response_json):
    if response_json:
        return response_json.get('message', 'Unknown error')
    return None