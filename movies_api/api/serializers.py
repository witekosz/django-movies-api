from rest_framework import serializers

from movies_api.models import Movie, Comment


class MovieTitleSerializer(serializers.Serializer):
    """
    Serializer for validation movie title
    """
    title = serializers.CharField()


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
