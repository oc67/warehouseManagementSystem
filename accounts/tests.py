from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from accounts.models import Organisation

# Create your tests here.


class UsersManagersTests(TestCase):
    def test_create_user(self):

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
        self.assertEqual(user.first_name, "Mike")
        self.assertEqual(user.last_name, "Rogers")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.work_email, "testuser@example.com")
        self.assertEqual(user.organisation.trading_name, "TestCompany")
  
  

    def test_create_superuser(self):
        # Create Organisation instance:
        organisation = Organisation.objects.create(trading_name="TestSuperCompany",
                                                   registered_name="TestSuperCompany",
                                                   industry="Defence",
                                                   is_up_to_date_in_payments=False)

        User = get_user_model()
        admin_user = User.objects.create_superuser(

            first_name="James",
            last_name="Robisons",
            username="testuser",
            work_email="superuser@example.com",
            password="testpassuperuser1234",
            organisation=organisation,      

        )
        self.assertEqual(admin_user.first_name, "James")
        self.assertEqual(admin_user.last_name, "Robisons")
        self.assertEqual(admin_user.username, "testuser")       
        self.assertEqual(admin_user.work_email, "superuser@example.com")
        self.assertEqual(admin_user.organisation.trading_name, "TestSuperCompany")
  


#class SignUpPageTests(TestCase):
#
#    def test_url_exists_at_correct_location_signupview(self):
#        response = self.client.get("/accounts/signup/")
#        self.assertEqual(response.status_code, 200)
#
#    def test_signup_view_name(self):
#        response = self.client.get(reverse("signup"))
#        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response, "registration/signup.html")
#
#    def test_signup_form(self):
#
#        organisation = Organisation.objects.create(companyName="TestSuperCompany")
#
#        response = self.client.post(
#            reverse("signup"),
#            {
#                "username": "testuser",
#                "email": "testuser@gmail.com",
#                "password1": "ACS123!acs",
#                "password2": "ACS123!acs",
#                "company": organisation.id,
#            },
#        )
#        self.assertEqual(response.status_code, 302)
#        self.assertEqual(get_user_model().objects.all().count(), 1)
#        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
#        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@gmail.com")
#