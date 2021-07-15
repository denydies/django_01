from rest_framework import serializers

from sport_blog.models import Post


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'content',
        )
