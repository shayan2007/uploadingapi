from django.urls import include, path

urlpatterns = [
    path('api/', include('file_upload_api.urls')),
]
