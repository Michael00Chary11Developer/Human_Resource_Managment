from django.db import models
import random


class Personnel(models.Model):
    """
    A model representing personnel information.

    This model stores various details about the personnel including
    personal information, educational background, career records,
    and employment details. Each personnel has a unique identifier
    generated automatically in the format '100XXX'.
    """
    

    def create_new_number_of_personnel():
        
            random_number = random.randint(1, 20)
            costum_format = f"100{random_number:03d}"

            if not Personnel.objects.filter(number_of_personnel=costum_format).exists():

                return  costum_format

    number_of_personnel = models.CharField(
        max_length=100, 
        blank=True, 
        editable=False, 
        unique=True, 
        default=create_new_number_of_personnel
        )

    """
    Unique personnel number generated in the format '100-XXX'.
    Automatically assigned upon creation.
    """

    # Personnel information
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    birth_date = models.DateField()

    # Educational records
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)

    # Career records
    career_records = models.TextField()

    # Position and level
    position = models.CharField(max_length=100)
    level_for_position = models.CharField(max_length=100)

    # Date when the personnel was employed.
    date_of_employment = models.DateField()

    def __str__(self):

        return f"{self.number_of_personnel} - {self.firstname} - {self.lastname}"

    """
        String representation of the Personnel model.
        
        Returns:
            str: A string in the format 'number_of_personnel - firstname - lastname'.
        """
