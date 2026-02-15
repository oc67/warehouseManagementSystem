from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Organisation,CustomUser

class UserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=UserCreationForm.Meta.fields+("work_email",)
        
class UserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields


