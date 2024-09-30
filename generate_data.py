from faker import Faker
import random
from uuid import uuid4
import panda as pd
from datetime import datetime 

fake = Faker()

def generate_cusomers_data(num_customers=1000):
    customers_data = []
    for i in num_customers:
        customer = {
            'customer_id': str(uuid4()),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'address': fake.address(),
            'city': fake.city(),
            'state': fake.state(),
            'country': fake.country(),
            'postal_code': fake.postcode(),
            'date_of_birth': fake.date_of_birth(),
            'account_balance': round(random.uniform(100, 10000), 2),
            'created_at': fake.date_time_this_year()
        }
        customers_data.append(customer)
    return customers_data