from rest_framework import serializers

from medium.models import Article


class ApiCreate(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'author__name',
            'description',
            'slug',
            'body',
            'created_at',
            'category',
            # 'tags',
            'image',
        ]
