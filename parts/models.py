from django.db import models

# Create your models here.
class Parts(models.Model):



    part_ID=models.BigAutoField(primary_key=True)
    part_name=models.CharField(max_length=50,null=False,blank=False)

    part_categories_list=[["Raw materials"],
                          "Fasteners",
                          "Connectors",
                          "Consumables",
                          "Mechanical components",
                          "Electrical components",
                          "Electronic components",
                          "Hardware",
                          "Assemblies",
                          "Subassemblies",
                          "Packaging materials",
                          ]
    part_category=models.CharField(choices=part_categories_list,null=False,blank=False)
    part_location=models.ManyToManyField("warehouse.Warehouse")