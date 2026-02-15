from django.urls import path
from .views import PartsListView

urlpatterns=[
    path("",PartsListView.as_view(),name="partsList")
]