import shutil
from rest_framework import serializers
from .models import Upload_Files, Store_Folder
serializers.ModelSerializer.create

class FolderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store_Folder
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Upload_Files
        fields = '__all__'

class FileListSerializer(serializers.Serializer):
    file = serializers.ListField(
        child = serializers.FileField(max_length = 100000 , allow_empty_file = False , use_url = False)
    )
    folder = serializers.CharField(required = False)
    
    def zip_files(self,folder):
        shutil.make_archive(f'public/static/zip/{folder}' , 'zip' ,f'public/static/{folder}' )

    def create(self , validated_data):
        folder = Store_Folder.objects.create()
        files = validated_data.pop('file')
        
        # files_objs = []
        for file in files:
            files_obj = Upload_Files.objects.create(folder = folder , file = file)
            # files_objs.append(files_obj)

        
        self.zip_files(folder.uid)


        return {'file' : files , 'folder' : str(folder.uid)}