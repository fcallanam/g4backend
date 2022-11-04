from django.urls import path
from . import views 

urlpatterns = [
    path("", views.halloffameView, name= "halloffame"),
]