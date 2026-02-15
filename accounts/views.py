from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy

from .forms import UserCreationForm

# Create your views here.



class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy("login")
    template_name="registration/signup.html"


