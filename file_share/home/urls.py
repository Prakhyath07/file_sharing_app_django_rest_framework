from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    
    path('', views.fileUpload.as_view(), name= 'upload'),
    path('<str:pk>/', views.FileDownloadListAPIView.as_view(), name= 'download')
]
