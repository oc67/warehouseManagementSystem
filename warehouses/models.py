from django.db import models
from accounts.models import Organisation

# Create your models here.

class Warehouse(models.Model):
    warehouse_ID = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100, null=False, blank=False)
    manager_full_name=models.CharField(max_length=150, null=True, blank=True)

    country=models.CharField(max_length=100, null=False, blank=False)
    municipality=models.CharField(max_length=100, null=False, blank=False)
    address_line=models.CharField(max_length=500, null=False, blank=False)

    organisation=models.ForeignKey(Organisation, null=False, blank=False,on_delete=models.CASCADE)
    is_active=models.BooleanField(null=True,blank=True)
    is_location_for_receipts=models.BooleanField(null=True,blank=True)
    is_location_for_shipments=models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.name
