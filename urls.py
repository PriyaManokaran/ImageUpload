from django.urls import path
from uploadapp.views import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view())
]