from django.views import View
from django.shortcuts import render

class FileUploadView(View):
    template_name = 'upload_form.html'

    def get(self, request, *args, **kwargs):
        # Handle GET request, render the upload form template
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('files')

        for file in files:
            # Save each file to the media folder or perform any other desired operation
            with open('media/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        return JsonResponse({'success': True})
