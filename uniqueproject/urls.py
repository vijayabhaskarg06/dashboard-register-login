from django.contrib import admin
from django.urls import path
from unique import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landingp, name='landing'),
    path('rege/',views.register,name='rege'),
    path('log/',views.login,name='logg'),
]
