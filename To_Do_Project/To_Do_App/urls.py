from django.urls import path
from To_Do_App import views

urlpatterns = [
    path('', views.Main)
]