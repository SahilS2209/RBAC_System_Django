from rest_framework import serializers
from .models import MyUser, API, Role

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = MyUser  
        fields = ['username', 'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')  
        user = MyUser(**validated_data)
        user.set_password(password)  
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  
        if password is not None:
            instance.set_password(password)  
        return super().update(instance, validated_data)

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = '__all__'
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'role', 'mapped_apis']