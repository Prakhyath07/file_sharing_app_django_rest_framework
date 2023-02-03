from django.shortcuts import render
from rest_framework import generics
from .models import Upload_Files
from .serializers import FileListSerializer

# Create your views here.
class fileUpload(generics.ListCreateAPIView):
    queryset = Upload_Files.objects.all()
    serializer_class = FileListSerializer