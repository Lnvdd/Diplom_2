class OrderData:
    
    VALID_INGREDIENTS = [
        '61c0c5a71d1f82001bdaaa6d',  
        '61c0c5a71d1f82001bdaaa6e'   
    ]
    
    SINGLE_INGREDIENT = ['61c0c5a71d1f82001bdaaa6d']
    
    INVALID_INGREDIENT = 'invalid_hash_12345'
    
    @staticmethod
    def order_with_multiple_ingredients():
        return {
            'ingredients': OrderData.VALID_INGREDIENTS
        }
    
    @staticmethod
    def order_with_one_ingredient():
        return {
            'ingredients': OrderData.SINGLE_INGREDIENT
        }
    
    @staticmethod
    def order_without_ingredients():
        return {
            'ingredients': []
        }
    
    @staticmethod
    def order_with_invalid_ingredient():
        return {
            'ingredients': [OrderData.INVALID_INGREDIENT]
        }
    
    @staticmethod
    def order_with_mixed_ingredients():
        return {
            'ingredients': OrderData.VALID_INGREDIENTS + [OrderData.INVALID_INGREDIENT]
        }