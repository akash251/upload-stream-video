
from django.urls import path
from .views import UploadVideoApiView

urlpatterns = [
    path('/', UploadVideoApiView.as_view()),
]
