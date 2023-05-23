from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class FileUploadView(APIView):
    def get(self, request, format=None):
        return render(request, 'file_upload/upload.html')

    def post(self, request):
        file = request.FILES['file']
        file_storage = FileSystemStorage()
        filename = file_storage.save(file.name, file)
        file_url = file_storage.url(filename)

        # Rest of your code

        return Response({'file_url': file_url})

