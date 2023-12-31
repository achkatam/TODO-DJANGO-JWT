from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Todo


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True,
                                     'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        existing_email = User.objects.filter(
            email=validated_data.get('email')
        ).first()

        if existing_email:
            raise serializers.ValidationError({'email': ['Email address is already in use.']})

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return {
            'username': user.username,
            'email': user.email,
        }


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
