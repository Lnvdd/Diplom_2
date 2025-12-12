BASE_URL = 'https://stellarburgers.education-services.ru'

ENDPOINTS = {
    'register': '/api/auth/register',  
    'login': '/api/auth/login',        
    'register_user': '/api/auth/register',
    'login_user': '/api/auth/login',
    'delete_user': '/api/auth/user',
    'update_user': '/api/auth/user',
    'logout': '/api/auth/logout',
    'user': '/api/auth/user',
    'create_order': '/api/orders',
    'user_orders': '/api/orders',
    'get_orders': '/api/orders/all',
    'get_ingredients': '/api/ingredients',
    'delete_order': '/api/orders',
}

STATUS_CODES = {
    'ok': 200,
    'created': 201,
    'bad_request': 400,
    'unauthorized': 401,
    'forbidden': 403,
    'not_found': 404,
    'conflict': 409,
    'server_error': 500,
}

VALID_INGREDIENT_HASHES = [
    '61c0c5a71d1f82001bdaaa6d',
    '61c0c5a71d1f82001bdaaa6e',
]

INVALID_INGREDIENT_HASH = 'invalid_hash_12345'