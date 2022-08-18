from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            contact = validated_data['contact'],
            nickname = validated_data['nickname'],
            privillege = validated_data['privillege'],
            password = validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'contact', 'nickname', 'privillege', 'password']