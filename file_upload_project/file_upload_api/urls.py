from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for your app

    # URL pattern for the file upload API
    path('upload/', views.FileUploadView.as_view(), name='file-upload'),
]
