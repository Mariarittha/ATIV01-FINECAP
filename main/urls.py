
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("reservas.urls", namespace="reservas")),
    path("", include("stand.urls", namespace="stand")),
]

