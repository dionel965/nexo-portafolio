from django.urls import path
from . import views

app_name = "atlas"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("estoicismo/", views.estoicismo, name="estoicismo"),
    path("existencialismo/", views.existencialismo, name="existencialismo"),
    path("etica/", views.etica, name="etica"),
    path("tecnologia/", views.tecnologia, name="tecnologia"),
]