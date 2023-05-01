import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

from faker import Faker
from second_app.models import User


faker=Faker()
def popo(n=5):
    for i in range(n):
        
        fname=faker.name().split()
        firstName=fname[0]
        lname=fname[1]
        email=faker.email()
        
        userdata=User.objects.get_or_create(first_name=firstName,last_name=lname,email=email)[0    ]
        

print(popo(20))