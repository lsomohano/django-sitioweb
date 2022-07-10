from django.urls import path

#from . import views
from .views import VRegistro, log_out, log_in

urlpatterns = [
    path('',VRegistro.as_view(),name="Autenticacion"),
    path('log_out',log_out, name="Log_Out"),
    path('log_in',log_in, name="Log_In"),
]