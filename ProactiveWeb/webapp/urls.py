from django.urls import path
from webapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("personalData", views.personalData, name="personalData"),
    path("mainTask/<int:page>", views.mainTask, name="mainTask"),
    path("rate/<int:page>", views.rate, name="rate"),
    path("ending", views.ending, name="ending"),
]
