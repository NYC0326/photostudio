from rest_framework import serializers
from .models import CategoryStudio
from studio.models import Studio

class CategoryStudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryStudio
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['studio_category'] = StudioRepresentationSerializer(read_only=True)
        return super(CategoryStudioSerializer, self).to_representation(instance)

class StudioRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('id', 'studio_name')