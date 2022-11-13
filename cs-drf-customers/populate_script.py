import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from apps.customer.models import Customer

def create_customers(quantity_customers):
    fake = Faker('pt_BR')
    fake.seed(10)
    for _ in range(quantity_customers):
        cpf = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) )
        phone = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        active = random.choice([True, False])
        p = Customer(name=name, email=email, cpf=cpf, rg=rg, phone=phone, active=active)
        p.save()

create_customers(50)
