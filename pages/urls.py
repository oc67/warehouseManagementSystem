from django.urls import path
from .views import HomePageView#,SignUpView, LoginView

urlpatterns=[
    path("",HomePageView.as_view(),name="home"),

]