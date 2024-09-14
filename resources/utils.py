from random import randint
from django.db import models


class CreateUniqueCode:

    def generate_unique_code(self:models.Model):
        while True:
            random_number = randint(1, 100)
            create_number = f'20000{random_number:03d}'
            if not self.objects.filter(asset_code=create_number).exists():
                return create_number        
