from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.fileUpload.as_view(), name= 'home')
]
