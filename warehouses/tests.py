from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from accounts.models import Organisation
from .models import Warehouse

# Create your tests here.


class WarehouseCreationTests(TestCase):
    
    def setUp(self):

        # Create Organisation instance:
        organisation = Organisation.objects.create(trading_name="TestCompany",
                                                   registered_name="TestCompany",
                                                   industry="Defence",
                                                   is_up_to_date_in_payments=False)

        User = get_user_model()
        user = User.objects.create_user(
            first_name="Mike",
            last_name="Rogers",
            username="testuser",
            work_email="testuser@example.com",
            password="testpass1234",
            organisation=organisation,
        )
    

    def WarehouseCreationTest(self):

        warehouse=Warehouse.objects.create(
                                            name="WarehouseTest",
                                            country="Spain",
                                            municipality="Madrid",
                                            address_line="Main Street, 1"
                                            organisation=self.organisation,
                                            is_active=True,
                                            is_location_for_receipts=True,
                                            is_location_for_shipments=True,
                                            manager_full_name="James Sott",

                                            )


        self.assertEqual(warehouse.name, "WarehouseTest")
        self.assertEqual(warehouse.country, "Spain")
        self.assertEqual(warehouse.muncipality, "Madrid")
        self.assertEqual(warehouse.address_line, "Main Street, 1")
        self.assertEqual(warehouse.organisation, self.organisation) 
        self.assertEqual(warehouse.is_active, True)
        self.assertEqual(warehouse.is_location_for_receipts, True)
        self.assertEqual(warehouse.is_location_for_shipments, True)
        self.assertEqual(warehouse.manager_full_name, "James Sott")


    def test_new_warehouse_url_exists_at_correct_location(self):
        response=self.client.get("warehouses/new")
        self.assertEqual(response.status_code, 200)


    def test_warehouse_creation_menu_url_available_by_name(self):
        response=self.client.get(reverse("new"))
        self.assertEqual(response.status_code,200)
    
    def test_warehouse_creation_template_name_correct(self):
        response=self.client.get(reverse("new"))
        self.assertTemplateUsed(response,"warehouse/warehouse_create.html")

    def test_warehouse_creation_template_name_correct(self):
        response=self.client.get(reverse("home"))
        self.assertContains(response,"<h1>Create a warehouse</h1>")

 
 
  
class WarehouseListTests(TestCase):
    def setUp(self):

        # Create Organisation instance:
        organisation = Organisation.objects.create(trading_name="TestCompany",
                                                   registered_name="TestCompany",
                                                   industry="Defence",
                                                   is_up_to_date_in_payments=False)

        User = get_user_model()
        user = User.objects.create_user(
            first_name="Mike",
            last_name="Rogers",
            username="testuser",
            work_email="testuser@example.com",
            password="testpass1234",
            organisation=organisation,
        )
    

        warehouse=Warehouse.objects.create(
                                            name="WarehouseTest",
                                            country="Spain",
                                            municipality="Madrid",
                                            address_line="Main Street, 1"
                                            organisation=organisation,
                                            is_active=True,
                                            is_location_for_receipts=True,
                                            is_location_for_shipments=True,
                                            manager_full_name="James Sott",

                                            )




    def test_warehouse_list_url_exists_at_correct_location(self):
        response=self.client.get("warehouses/list")
        self.assertEqual(response.status_code, 200)


    def test_warehouse_list_menu_url_available_by_name(self):
        response=self.client.get(reverse("list"))
        self.assertEqual(response.status_code,200)
    
    def test_warehouse_creation_template_name_correct(self):
        response=self.client.get(reverse("list"))
        self.assertTemplateUsed(response,"warehouse/warehouse_list.html")

    def test_warehouse_creation_template_name_correct(self):
        response=self.client.get(reverse("home"))
        self.assertContains(response,"<h1>Warehouse list</h1>")


#class WarehouseDetailTests(TestCase):
#    def setUp(self):
#
#        # Create Organisation instance:
#        organisation = Organisation.objects.create(trading_name="TestCompany",
#                                                   registered_name="TestCompany",
#                                                   industry="Defence",
#                                                   is_up_to_date_in_payments=False)
#
#        User = get_user_model()
#        user = User.objects.create_user(
#            first_name="Mike",
#            last_name="Rogers",
#            username="testuser",
#            work_email="testuser@example.com",
#            password="testpass1234",
#            organisation=organisation,
#        )
#    
#
#        warehouse=Warehouse.objects.create(
#                                            name="WarehouseTest",
#                                            location="Madrid",
#                                            organisation=organisation)
#
#        self.assertEqual(warehouse.name, "WarehouseTest")
#        self.assertEqual(warehouse.location, "Madrid")
#        self.assertEqual(warehouse.organisation, organisation) 
#
#
#    def test_warehouse_list_url_exists_at_correct_location(self):
#        response=self.client.get("warehouses/list")
#        self.assertEqual(response.status_code, 200)
#
#
#    def test_warehouse_list_menu_url_available_by_name(self):
#        response=self.client.get(reverse("list"))
#        self.assertEqual(response.status_code,200)
#    
#    def test_warehouse_creation_template_name_correct(self):
#        response=self.client.get(reverse("list"))
#        self.assertTemplateUsed(response,"warehouse/warehouse_detail.html")
#
#    def test_warehouse_creation_template_name_correct(self):
#        response=self.client.get(reverse("home"))
#        self.assertContains(response,"<h1>Warehouse</h1>")






























