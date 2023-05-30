from rest_framework import serializers
from apps.users.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"

    def create(self, validated_data):
        user = MyUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class MyUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'email': instance['email'],
            'username': instance['username'],
            'password': instance['password']
        }
