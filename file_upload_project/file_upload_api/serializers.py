from rest_framework import serializers
from file_upload_api.models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('id', 'file', 'uploaded_at')
