from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("atlas/", include("atlas.urls")),
    path("", include("portafolio.urls")),
]

