from faker import Faker
import string
import random

class RandomUtil:
    def __init__(self):
        self.faker=Faker()
    
    def get_random_firstname(self)->str:
        return self.faker.file_name()
    
    def get_random_lastname(self)->str:
        return self.faker.last_name()
    
    def get_random_fullname(self)->str:
        return self.faker.full_name()
    
    def get_random_email(self)->str:
        return self.faker.email()
    
    def get_random_phoneNumber(self)->str:
        return self.faker.phone_number()
    
    def get_random_username(self)->str:
        return self.faker.user_name()
    
    def get_random_password(self)->str:
        return self.faker.password(length=10)
    
    def get_random_country(self)->str:
        return self.faker.country()
    
    def get_random_state(self)->str:
        return self.faker.state()
    
    def get_random_city(self)->str:
        return self.faker.city()
    def get_random_pin(self)->str:
        return self.faker.postcode()
    
    def get_random_address(self) -> str:
        return self.faker.street_address()

    def get_random_alphanumeric(self, length: int) -> str:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def get_random_numeric(self, length: int) -> str:
        return ''.join(random.choice(string.digits) for _ in range(length))

    def get_random_uuid(self) -> str:
        return str(self.faker.uuid4())
        
    
    
    