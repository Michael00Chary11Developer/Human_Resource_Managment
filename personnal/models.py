from django.db import models
import random



class Personnal(models.Model):
    
    def create_new_number_of_personnal():
        while True:
            random_number = random.randint(1, 100)
            costum_format = f"100-{random_number:03d}"
            
            if not Personnal.objects.filter(number_of_personnal=costum_format).exists():
                
                return costum_format
    
    
    number_of_personnal = models.CharField(max_length=100,blank=True,editable=False, unique=True, default=create_new_number_of_personnal, db_index=True)
    # def save(self, *args, **kwargs):
    #     if not self.number_of_personnal:
    #         last_person = Personnal.objects.all().order_by('id').last()
    #         if last_person:
    #             last_number = int(last_person.number_of_personnal[4:])  
    #             self.number_of_personnal = f"100-{last_number + 1:03d}"  
    #         else:
    #             self.number_of_personnal = "100-001"  
    #     super().save(*args, **kwargs)
    
    
    
    
    """
        Personnel number    
    """
    
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone_number= models.CharField(max_length=100)
    birth_date = models.DateField()
    """
       Individual profile 
    """
    
    
    degree = models.CharField(max_length=100)
    fieldـofـstudy = models.CharField(max_length=100)
    """
        Educational records
    """
    
    Careerـrecords = models.TextField()
    """
        Career records
    """
    
    position = models.CharField(max_length=100)
    level_for_position = models.CharField(max_length=100)
    """
        position and level
    """
    
    Date_of_employment = models.DateField()
    
    
    def __str__(self):
        return f"{self.number_of_personnal} - {self.firstname} - {self.lastname}" 
      
    
      
    
    
    
    