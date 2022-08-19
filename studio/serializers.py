from rest_framework import serializers
from .models import Studio
from accounts.models import User
from question.serializers import QuestionSerializer
from photo.serializers import PhotoSerializer
from reserve.serializers import ReserveSerializer


class StudioSerializer(serializers.ModelSerializer):
    studio_question = QuestionSerializer(many=True, read_only=True)
    studio_portfolio = PhotoSerializer(many=True, read_only=True)
    studio_reserve = ReserveSerializer(many=True, read_only=True)

    class Meta:
        model = Studio
        fields = ('id', 'ceo_id', 'studio_name', 'location', 'post_num', 'info', 'intro', 'insta_id', 'studio_question', 'studio_portfolio', 'studio_reserve')

    def to_representation(self, instance):
        self.fields['ceo_id'] = UserRepresentationSerializer(read_only=True)
        return super(StudioSerializer, self).to_representation(instance)

class UserSerializer(serializers.ModelSerializer):
    ceo_id = StudioSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'contact', 'nickname', 'ceo_id')

class UserRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('contact', 'email', 'privillege')