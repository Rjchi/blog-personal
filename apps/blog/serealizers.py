from rest_framework import serializers

from . import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = [
            'id',
            'title',
            'slug',
            'thumbnail',
            'excerpt',
            'description',
            'published',
            'views',
            'time_red',
            'category',
        ]