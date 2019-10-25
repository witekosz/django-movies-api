from rest_framework import serializers

from movies_api.models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for movie models
    """

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for movie models
    """

    class Meta:
        model = Comment
        fields = '__all__'
