from rest_framework import serializers
from .models import Reserve
from accounts.models import User
from studio.models import Studio

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['reserver'] = UserRepresentationSerializer(read_only=True)
        self.fields['studio_reserve'] = StudioRepresentationSerializer(read_only=True)
        return super(ReserveSerializer, self).to_representation(instance)

class UserRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'contact', 'email')

class StudioRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('id', 'studio_name')