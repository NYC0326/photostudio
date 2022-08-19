from rest_framework import serializers
from .models import Answer
from accounts.models import User
from question.models import Question

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question_id', 'user_answer_id', 'reply')

    def to_representation(self, instance):
        self.fields['question_id'] = QuestionRepresentationSerializer(read_only=True)
        self.fields['user_answer_id'] = UserRepresentationSerializer(read_only=True)
        return super(AnswerSerializer, self).to_representation(instance)

class QuestionRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title')

class UserRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')