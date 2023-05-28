from rest_framework.views import APIView
from django.http import StreamingHttpResponse
from upload.models import Video


class VideoStreamingApiView(APIView):
    def get(self, request, pk):
        video = Video.objects.get(title=pk)
        video_file = video.video_file
        response = StreamingHttpResponse(video_file.open(), content_type='video/mp4')
        response['Content-Disposition'] = 'inline; filename="{}.mp4"'.format(video.title)
        print(response.streaming)
        return response
