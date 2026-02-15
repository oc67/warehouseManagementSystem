from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Organisation

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    model=CustomUser
    list_display=[
     "username",
     "work_email",
     "organisation"
     ]
    fieldsets=UserAdmin.fieldsets+((None, {"fields":("work_email","organisation")}),)
    add_fieldsets=UserAdmin.add_fieldsets+((None, {"fields":("work_email","organisation")}),)

class OrganisationAdmin():
    list_display=[
        ""
    ]

admin.site.register(CustomUser,CustomUserAdmin)
#admin.site.register(Organisation,CustomUserAdmin)

