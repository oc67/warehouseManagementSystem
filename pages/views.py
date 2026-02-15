from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy


# Create your views here.

class HomePageView(TemplateView):
    template_name="home.html"


