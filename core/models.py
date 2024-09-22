from django.db import models
from django.contrib.auth.models import User

class BaseModelDate(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    class Meta:
        abstract=True
        
   
        
   