from rest_framework import serializers
from .models import Studio
from accounts.models import User

# ModelSerializer
class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('studio_name', 'contact', 'location', 'post_num')

class UserSerializer(serializers.ModelSerializer):
    studio = StudioSerializer(read_only=True)

