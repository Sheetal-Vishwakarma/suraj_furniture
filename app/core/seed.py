from .models import Gallery
from faker import Faker

fake = Faker()

def seed_db(n):
    for i in range(0, n):
        print(f"Name : {fake.name()}")
        # Gallery.objects.create(
        #     name = fake.name(),
        #     image_name = '',
        #     status = '1'
        # )

