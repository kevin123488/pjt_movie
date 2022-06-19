from rest_framework import serializers
from django.contrib.auth import get_user_model
from communitys.models import Review
from movies.models import Movie


class ProfileSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = ('pk', 'review_title', 'content')

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path')

    like_reviews = ReviewSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'reviews', 'like_reviews', 'like_movies', 'genre1', 'genre2', 'genre3', 'genre4', 'followings', 'followers',)