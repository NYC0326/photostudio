from pickletools import read_long1
from rest_framework import serializers
from .models import Studio
from accounts.models import User

# ModelSerializer
class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        # fields = ('studio_name', 'contact', 'location', 'post_num')
        fields = ('id', 'ceo', 'studio_name', 'location', 'post_num')

    def to_representation(self, instance):
        self.fields['ceo'] = UserRepresentationSerializer(read_only=True)
        return super(StudioSerializer, self).to_representation(instance)

class UserSerializer(serializers.ModelSerializer):
    studio = StudioSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('ceo_id')

class UserRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('contact', 'email', 'privillege')