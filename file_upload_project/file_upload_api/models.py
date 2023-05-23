from django.db import models

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'file_upload_api'