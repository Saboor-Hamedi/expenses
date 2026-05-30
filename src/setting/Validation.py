
class Validation:
    def __init__(self,
                 price:  float | int   | None = None,
                 name: str | None = None,
                 amount: int | None = None
                 ):
        self.price = price
        self.name = name
        self.amount = amount

    def validate_price(self, price, strict=True) -> bool:

        # This handles intentional null values first
        if not strict and (price is None or price == ''):
            return True
        try:
            # This conversion to safely isolate non-numeric inputs
            numeric_price= float(price)
        except (ValueError, TypeError):
            print('Price can be only number! ')
            return False

        if numeric_price <= 0:
            return False
        return True
    def validate_name(self, name, strict=True) -> bool:
        # check if the name is none of empty
        if not strict and (name is None or name == ''):
            return True
        # We need to set try: catch in order someone inserts number
        # This makes sure the name is always text
        try:
            if not isinstance(name, str):
                return False
            if name.isdigit():
                print('Name cannot be a number! ')
                return False
            return True


        except (ValueError, TypeError):
            print('Name can be only text! ')
            return False

    def validate_amount(self, amount, strict=True) -> bool:
        # check if the name is none of empty
        if not strict and (amount is None or amount == ''):
            return True

        try:
            numeric_amount = int(amount)
        except (ValueError, TypeError):
            print('Amount can be only number!')
            return False
        if numeric_amount <= 0:
            return False
        return True



if __name__ == '__main__':
    validate = Validation(10)
    print(validate.validate_price("Hello world"))  # True (Valid string float)
    print(validate.validate_price(10, strict=False))  # True (Valid integer)
    print(validate.validate_price(None))  # True (Valid intentional null)
    print(validate.validate_price(""))  # True (Valid empty string null)
    print(validate.validate_price(0))  # False (Must be greater than 0)
    print(validate.validate_price(-5))  # False (Must be greater than 0)
    print(validate.validate_price("abc"))  # False (Invalid string text)

    print('---------- Name validation-------------------')
    print(validate.validate_name("Hello world", strict=False))  # True (Valid string)
    print(validate.validate_name(None, strict=False)) # True
    print(validate.validate_name(10, strict=False)) # False
    print(validate.validate_name("", strict=False)) # True

    print('---------- Amount validation-------------------')
    print(validate.validate_amount("Hello world"))  # True (Valid string float)
    print(validate.validate_amount(10))  # True (Valid integer)
    print(validate.validate_amount(None, strict=False))  # True (Valid intentional null)
    print(validate.validate_amount(None))  # True (Valid intentional null)
    print(validate.validate_amount(""))  # True (Valid empty string null)

