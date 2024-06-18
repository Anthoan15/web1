from django.urls import path
from . import views


urlpatterns = [

    path('', views.authenticated, name="Authenticated"),
    path('cerra_sesion', views.cerra_sesion, name="cerra_sesion"),
    path('logear', views.logear, name="logear"),

  
]



