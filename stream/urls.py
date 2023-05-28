
from django.urls import path
from .views import VideoStreamingApiView

urlpatterns = [
    path('', VideoStreamingApiView.as_view()),
]
