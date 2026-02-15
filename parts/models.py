from django.db import models

# Create your models here.
class Parts(models.Model):



    part_ID=models.BigAutoField(primary_key=True)
    part_name=models.CharField(max_length=100,null=False,blank=False)

    part_categories_list=[["Raw materials","Raw materials"],
                          ["Fasteners","Fasteners"],
                          ["Connectors","Connectors"],
                          ["Consumables","Consumables"],
                          ["Mechanical components","Mechanical components"],
                          ["Electrical components","Electrical components"],
                          ["Electronic components","Electronic components"],
                          ["Hardware","Hardware"],
                          ["Assemblies","Assemblies"],
                          ["Subassemblies","Subassemblies"],
                          ["Packaging materials","Packaging materials"],
                          ]
    part_category=models.CharField(choices=part_categories_list,max_length=100,null=False,blank=False)
    #part_location=models.ManyToManyField("warehouse.Warehouse")