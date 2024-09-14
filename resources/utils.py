from random import randint
from django.db import models


class CreateUniqueCode:
    @staticmethod
    def create_code(model_field: models, unique_code: str) -> str:
        while True:
            random_number = randint(1, 10000)
            create_code = f'1000{random_number:05d}'

            if not model_field.objects.filter(unique_code=create_code).exists():
                return create_code
