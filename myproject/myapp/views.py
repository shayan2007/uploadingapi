# views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class FileUploadView(APIView):
    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        if file_obj is None:
            return Response({'error': 'No file uploaded'}, status=400)

        # Validate the file (optional)
        # Implement your file validation logic here

        try:
            # Define the directory to save the file
            save_dir = 'path/to/save/directory/'

            # Construct the file path
            file_path = save_dir + file_obj.name

            # Save the file
            with open(file_path, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

            return Response({'message': 'File uploaded successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)
