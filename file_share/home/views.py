from django.shortcuts import render, redirect
from rest_framework import generics
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from .models import Upload_Files, Store_Folder
from .serializers import FileListSerializer, FolderSerializer
from wsgiref.util import FileWrapper
from rest_framework.reverse import reverse
import os

# Create your views here.
class fileUpload(generics.CreateAPIView):
    queryset = Upload_Files.objects.all()
    serializer_class = FileListSerializer




class FileDownloadListAPIView(generics.ListAPIView):
    serializer_class = FolderSerializer
    lookup_field = 'pk'

    def get(self, request, pk, format=None):
        queryset = Store_Folder.objects.get(pk=pk)
        file_uid = queryset.uid
        file_path = os.path.join(f'C:/ineuron/Django/django_web_development/file_sharing_app_django_rest_framework/file_share/public/static/zip/{file_uid}.zip')
        document = open(file_path, 'rb')
        # response = HttpResponse(FileWrapper(document), content_type='application/msword')
        # response['Content-Disposition'] = 'attachment; filename="%s.zip"' % file_uid
        # return response
        # send file
        # file_handle = file_path.open()
        response = FileResponse(document, content_type='whatever')
        response['Content-Disposition'] = 'attachment; filename="%s.zip"' % file_uid

        return response

