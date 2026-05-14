from django.contrib import admin
from django.urls import path
from app.views import index

# URL Routing
urlpatterns = [
    path('admin/', admin.site.urls), # Admin portal
    path('', index, name='index'),    # Home page
]
