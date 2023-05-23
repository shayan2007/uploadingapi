from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UploadedFileSerializer

class FileUploadView(APIView):
    def get(self, request, format=None):
        return render(request, 'file_upload/upload.html')

    def post(self, request, format=None):
        serializer = UploadedFileSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
