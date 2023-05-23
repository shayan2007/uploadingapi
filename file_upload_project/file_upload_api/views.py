from rest_framework import generics
from file_upload_api.models import FileUpload
from file_upload_api.serializers import FileUploadSerializer

class FileUploadView(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
