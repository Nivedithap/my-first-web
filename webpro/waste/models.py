from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    product_date = models.DateTimeField('date added',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    activate = models.BooleanField(max_length=50,default=False)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/',max_length=255,null=True,blank=True)

    def _str_(slef):
        return self.product_name
