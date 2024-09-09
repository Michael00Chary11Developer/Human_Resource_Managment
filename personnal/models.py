from django.db import models
import uuid



class Personnal(models.Model):
    
    
    
    number_of_personnal = models.CharField(max_length=100,blank=True, null=True, )
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
    level_fo_position = models.CharField(max_length=100)
    """
        position and level
    """
    
    Date_of_employment = models.DateField()
    
    
    def ___str__(self):
        return f"{self.number_of_personnal} - {self.firstname} - {self.lastname}" 
      
    
      
    
    
    
    