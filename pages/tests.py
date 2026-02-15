
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your tests here.

#Tests use CamelCase because unittest is based on jUnit from Java.

class HomePageTests(SimpleTestCase):

    #ensure valid page exists at url specified
    def test_url_exists_at_correct_location(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code, 200)

    #checks name given to URL matches name rendered

    def test_url_available_by_name(self):
        response=self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
    
    def test_template_name_correct(self):
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"home.html")

    def test_template_name_correct(self):
        response=self.client.get(reverse("home"))
        self.assertContains(response,"<h1>Warehouse management system</h1>")
