from rest_framework import serializers
from .models import Question
from studio.models import Studio
from accounts.models import User
from answer.serializers import AnswerSerializer

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'studio_id', 'user_question_id', 'title', 'date', 'question', 'answer')

    def to_representation(self, instance):
        self.fields['studio_id'] = StudioRepresentationSerializer(read_only=True)
        self.fields['user_question_id'] = UserRepresentationSerializer(read_only=True)
        return super(QuestionSerializer, self).to_representation(instance)

class UserRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class StudioRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('id', 'studio_name')