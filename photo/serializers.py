from rest_framework import serializers
from .models import Photo
from question.serializers import StudioRepresentationSerializer

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['studio_portfolio'] = StudioRepresentationSerializer(read_only=True)
        return super(PhotoSerializer, self).to_representation(instance)
  