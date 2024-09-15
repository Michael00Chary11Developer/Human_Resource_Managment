from random import randint
from django.db import models

"""
class:CreateUnique code:have function generate uniq code:
    method:generate_unique_code
        genrate code by random
        randint method that select number beetween 1 to 100
    fields of method:
        random_number(int) get random number if randint that select beetween 1 to 100
        create_number(str) 20000+random number 
        if number not have 3 digit 
        generate zero 
    example:
        random_number(int)=12
        create_number(str)=20000_012
"""


class CreateUniqueCode:

    def generate_unique_code(self: models.Model):
        try:
            while True:
                random_number = randint(1, 100)
                create_number = f'20000{random_number:03d}'
                """
                The condition checks this number exists or not, and if it does, it returns a new number it can be stackoverflow 
                if all number exist => cannot genrate new code so The loop runs endlessly
                solution: create bigger number or put it in try except 
                if error occurer
                """
                if not self.objects.filter(asset_code=create_number).exists():
                    return create_number
        except:
            raise Exception(
                "Sorry", "All number has been generate!! for solution call to programmer!")
