from rest_framework import viewsets
from sport_blog.models import Post

from .generics import RateSerializer


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = RateSerializer
