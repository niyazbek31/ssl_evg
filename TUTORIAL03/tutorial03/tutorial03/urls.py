
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('', include('guests.urls')),
    path('api/',   include('rest_framework.urls')),

    path('admin/', admin.site.urls),
]