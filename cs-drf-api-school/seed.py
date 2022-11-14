import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from datetime import date
from apps.school.models import  Student, Course, Enrollment

def create_students(quantity):
    fake = Faker('pt_BR')
    fake.seed(10)
    for _ in range(quantity):
        cpf = CPF()
        name = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) )
        cpf = cpf.generate()
        birth_date = date(random.randrange(1980, 2006), random.randrange(1, 12), random.randrange(1, 28))
        a = Student(name=name,rg=rg, cpf=cpf,birth_date=birth_date)
        a.save()

def create_courses(quantity):
    fake = Faker('pt_BR')
    fake.seed(10)
    for i in range(quantity):
        code = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        descs = ['Python Fundamentos', 'Python intermediário','Python Avançado', 'Python para Data Science', 'Python/React']
        level = random.choice(Course.Level.choices)
        c = Course(code=code,description=descs[i], level=level[0])
        c.save()


create_students(200)
create_courses(5)