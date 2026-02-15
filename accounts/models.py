# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Organisation(models.Model):
    organisation_ID = models.BigAutoField(primary_key=True)
    trading_name=models.CharField(max_length=50, null=False, blank=False)
    registered_name=models.CharField(max_length=50, null=True, blank=True)
    industry = models.CharField(max_length=50, null=True, blank=True)
    is_up_to_date_in_payments=models.BooleanField(default=False,null=False, blank=False)

    def __str__(self):
        return self.trading_name


#Customers are expected to introduce work email--> find out company name 
class CustomUser(AbstractUser):
    user_ID=models.BigAutoField(primary_key=True)
    organisation=models.ForeignKey(Organisation,
                                   on_delete=models.CASCADE,  #  user is deleted when organisation is deleted
                                   related_name="organisations",
                                   null=True,
                                   blank=True,)
    first_name=models.CharField(max_length=100,null=False,blank=False) # already part of Abstract user, field to be removed
    last_name=models.CharField(max_length=100,null=False,blank=False) # already part of Abstract user, field to be removed
    work_email=models.EmailField(max_length=100,null=False,blank=False)


    def __str__(self):
        return self.first_name+self.last_name
