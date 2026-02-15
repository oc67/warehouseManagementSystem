from django.views.generic import ListView, TemplateView

# Create your views here.

class PartsListView(TemplateView):
    template_name="parts_list.html"
