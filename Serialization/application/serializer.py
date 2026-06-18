from rest_framework import serializers
from .models import MovieModels
class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieModels
        fields = ['sno','name','hero','heroine','director','music']
