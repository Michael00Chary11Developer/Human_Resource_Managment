from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid1

class BaseModelDate(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.PROTECT,default=uuid1)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    class Meta:
        abstract=True
        
    def save(self,*arg,**kwargs) :
        if self.pk is not None:
            self.update_at=timezone.now()
        return super().save(*arg,**kwargs)    