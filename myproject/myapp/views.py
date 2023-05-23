from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class FileUploadView(APIView):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request, format=None):
        file_objs = request.FILES.getlist('files')
        if len(file_objs) == 0:
            return Response({'error': 'No files uploaded'}, status=400)

        try:
            save_dir = r"C:\Users\Shayan'\\uploadingapi\myproject\saved_files"
            for file_obj in file_objs:
                file_path = save_dir + file_obj.name

                with open(file_path, 'wb+') as destination:
                    for chunk in file_obj.chunks():
                        destination.write(chunk)

            return Response({'message': 'Files uploaded successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)
